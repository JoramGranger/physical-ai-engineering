#!/usr/bin/env python3
"""Validate repository structure, documentation sections, and local Markdown links."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

COURSES = (
    "01-mathematical-foundations", "02-machine-learning", "03-deep-learning",
    "04-computer-vision", "05-3d-perception", "06-robotics",
    "07-ros2-and-simulation", "08-autonomous-systems", "09-agentic-ai",
    "10-embodied-ai", "11-edge-ai",
)
PROJECTS = (
    "image-classification", "object-detection-tracking", "3d-reconstruction",
    "robotic-arm", "autonomous-mobile-robot", "vision-guided-manipulation",
    "autonomous-drone",
)
COURSE_FILES = (
    "README.md", "syllabus.md", "learning-objectives.md", "resources.md",
    "exercises/README.md", "lectures/README.md", "assignments/README.md",
    "notes/README.md",
)
PROJECT_SECTIONS = (
    "Problem statement", "Learning objectives", "Prerequisites",
    "Proposed architecture", "Technologies", "Mathematical foundations",
    "Implementation milestones", "Testing strategy", "Evaluation metrics",
    "Expected deliverables", "Future improvements",
)
MONTH_SECTIONS = (
    "Learning objectives", "Mathematical concepts", "Topics and subtopics",
    "University lectures", "Recommended textbooks", "Practical exercises",
    "Programming assignment", "Hardware or simulation",
    "Projects and weekly sequence", "Parallel AI engineering",
    "Expected deliverables", "Assessment criteria",
)
ROOT_FILES = (
    "README.md", "ROADMAP.md", "CONTRIBUTING.md", "LICENSE", ".gitignore",
    "docs/curriculum.md", "docs/learning-journal.md", "docs/resources.md",
    "docs/environment.md", "docs/system-architecture.md",
    "docs/mathematics/README.md", "courses/README.md", "projects/README.md",
    "hardware/README.md", "infrastructure/README.md", "experiments/README.md",
    "experiments/TEMPLATE.md", "assets/README.md", "scripts/README.md",
    ".github/workflows/docs.yml", ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/documentation.yml",
    ".github/ISSUE_TEMPLATE/experiment.yml",
)
EXCLUDED = {".git", ".agents", ".aws", ".codex", ".venv", "venv", "node_modules", "__pycache__"}
DEST = r'(?P<dest><[^>\n]+>|[^\s)]+)'
INLINE_LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*' + DEST + r'(?:\s+["\'][^\n]*?["\'])?\s*\)')
REF_DEF = re.compile(r'^ {0,3}\[(?P<id>[^\]\n]+)\]:\s*' + DEST, re.MULTILINE)
REF_USE = re.compile(r'!?\[(?P<label>[^\]\n]+)\]\[(?P<id>[^\]\n]*)\]')
HEADING = re.compile(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', re.MULTILINE)


def visible_markdown(text: str) -> tuple[str, list[str]]:
    """Mask fenced blocks without changing line numbers; report unmatched fences."""
    marker: str | None = None
    width = 0
    opened = 0
    output = []
    for number, line in enumerate(text.splitlines(keepends=True), 1):
        fence = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line.rstrip('\r\n'))
        if marker is None and fence:
            marker, width, opened = fence[1][0], len(fence[1]), number
            output.append('\n' if line.endswith('\n') else '')
        elif marker is not None:
            if fence and fence[1][0] == marker and len(fence[1]) >= width and not fence[2].strip():
                marker = None
            output.append('\n' if line.endswith('\n') else '')
        else:
            output.append(line)
    issues = [f'line {opened}: unclosed fenced code block'] if marker else []
    return ''.join(output), issues


def anchors(text: str) -> set[str]:
    """GitHub-style slugs for ordinary ATX headings, including duplicate suffixes."""
    visible, _ = visible_markdown(text)
    counts: dict[str, int] = {}
    result = set()
    for heading in HEADING.findall(visible):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        heading = re.sub(r'<[^>]+>', '', heading)
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        result.add(f'{slug}-{number}' if number else slug)
    return result


def normalized_reference(label: str) -> str:
    return ' '.join(label.lower().split())


def local_links(root: Path, document: Path) -> list[str]:
    """Check inline and explicit/collapsed reference links in a single document."""
    root = root.resolve()
    document = document.resolve()
    label = document.relative_to(root).as_posix()
    visible, fence_issues = visible_markdown(document.read_text(encoding='utf-8'))
    issues = [f'{label}: {issue}' for issue in fence_issues]
    # Code examples are not destinations; preserve offsets/line numbers while masking.
    scan = re.sub(r'(`+)(.*?)\1', lambda m: re.sub(r'[^\n]', ' ', m[0]), visible, flags=re.DOTALL)
    definitions = {
        normalized_reference(m['id']): m['dest'].strip('<>')
        for m in REF_DEF.finditer(scan)
    }
    found = [(m.start(), m['dest'].strip('<>')) for m in INLINE_LINK.finditer(scan)]
    found.extend((m.start(), m['dest'].strip('<>')) for m in REF_DEF.finditer(scan))
    for match in REF_USE.finditer(scan):
        key = normalized_reference(match['id'] or match['label'])
        if key not in definitions:
            line = scan.count('\n', 0, match.start()) + 1
            issues.append(f'{label}:{line}: undefined reference [{key}]')
        # Definition destinations are checked once, even if unused.
    for offset, destination in found:
        line = scan.count('\n', 0, offset) + 1
        prefix = f'{label}:{line}: '
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc:
            continue
        path = unquote(parsed.path)
        if path.startswith('/'):
            issues.append(prefix + f'use a relative repository path: {destination}')
            continue
        target = (document.parent / path).resolve() if path else document
        if not target.is_relative_to(root):
            issues.append(prefix + f'link escapes repository: {destination}')
            continue
        if not target.exists():
            issues.append(prefix + f'missing destination: {destination}')
            continue
        if parsed.fragment:
            anchor_target = target / 'README.md' if target.is_dir() else target
            if anchor_target.suffix.lower() == '.md' and anchor_target.is_file():
                if unquote(parsed.fragment) not in anchors(anchor_target.read_text(encoding='utf-8')):
                    issues.append(prefix + f'missing heading fragment: {destination}')
    return issues


def structure_issues(root: Path) -> list[str]:
    required = list(ROOT_FILES)
    required.extend(f'courses/{course}/{file}' for course in COURSES for file in COURSE_FILES)
    required.extend(f'projects/{project}/README.md' for project in PROJECTS)
    required.extend(f'hardware/{part}/README.md' for part in (
        'esp32', 'sensors', 'mobile-robot', 'robotic-arm', 'aerial-robotics'))
    required.extend(f'infrastructure/{part}/README.md' for part in (
        'gpu-computing', 'model-serving', 'containers', 'edge-deployment'))
    issues = [f'missing required file: {file}' for file in required if not (root / file).is_file()]
    for project in PROJECTS:
        path = root / 'projects' / project / 'README.md'
        if path.is_file():
            visible, _ = visible_markdown(path.read_text(encoding='utf-8'))
            for section in PROJECT_SECTIONS:
                if not re.search(r'^## ' + re.escape(section) + r'\s*$', visible, re.MULTILINE):
                    issues.append(f'{path.relative_to(root)}: missing section: {section}')
    curriculum = root / 'docs/curriculum.md'
    if curriculum.is_file():
        visible, _ = visible_markdown(curriculum.read_text(encoding='utf-8'))
        blocks = list(re.finditer(r'^## Month (\d+)\b[^\n]*', visible, re.MULTILINE))
        if [int(m[1]) for m in blocks] != list(range(1, 13)):
            issues.append('docs/curriculum.md: expected Months 1–12 exactly once in order')
        for i, block in enumerate(blocks):
            body = visible[block.end():blocks[i + 1].start() if i + 1 < len(blocks) else len(visible)]
            for section in MONTH_SECTIONS:
                if not re.search(r'^### ' + re.escape(section) + r'\s*$', body, re.MULTILINE):
                    issues.append(f'docs/curriculum.md: Month {block[1]} missing section: {section}')
    return issues


def check_repository(root: Path) -> tuple[list[str], int]:
    root = root.resolve()
    documents = sorted(p for p in root.rglob('*.md') if not EXCLUDED.intersection(p.relative_to(root).parts))
    issues = structure_issues(root)
    for document in documents:
        issues.extend(local_links(root, document))
    return issues, len(documents)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error('repository root must be an existing directory')
    issues, count = check_repository(args.root)
    if issues:
        print('\n'.join(issues), file=sys.stderr)
        print(f'FAILED: {len(issues)} issue(s) across {count} Markdown files.', file=sys.stderr)
        return 1
    print(f'OK: {count} Markdown files; required structure, monthly/project sections, and local links passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
