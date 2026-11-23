"""Regression coverage for documentation failures that should block a push."""

from pathlib import Path
import tempfile
import unittest

from scripts.check_docs import anchors, local_links, structure_issues


class DocumentationChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def test_relative_links_encoded_spaces_and_images(self):
        self.write('docs/a file.md', '# Title\n')
        self.write('assets/plot.svg', '<svg/>')
        doc = self.write('README.md', '[A](docs/a%20file.md)\n[B](<docs/a file.md>)\n![plot](assets/plot.svg)\n')
        self.assertEqual(local_links(self.root, doc), [])

    def test_missing_link_reports_document_and_line(self):
        doc = self.write('README.md', '# Title\n\n[broken](docs/missing.md)\n')
        self.assertEqual(local_links(self.root, doc), ['README.md:3: missing destination: docs/missing.md'])

    def test_valid_and_missing_fragments_in_other_document(self):
        self.write('docs/guide.md', '# Guide\n## Assessment policy\n## Assessment policy\n')
        doc = self.write('README.md', '[ok](docs/guide.md#assessment-policy-1)\n[bad](docs/guide.md#absent)\n')
        issues = local_links(self.root, doc)
        self.assertEqual(len(issues), 1)
        self.assertIn('README.md:2: missing heading fragment', issues[0])

    def test_same_document_fragment_and_heading_slug(self):
        doc = self.write('README.md', '# A `model`: results!\n[ok](#a-model-results)\n')
        self.assertEqual(local_links(self.root, doc), [])
        self.assertEqual(anchors('# Repeat\n# Repeat\n'), {'repeat', 'repeat-1'})

    def test_code_examples_do_not_create_links_or_headings(self):
        doc = self.write('README.md', '# Real\n~~~md\n[example](missing.md)\n# Fake\n~~~\n`[inline](missing.md)`\n')
        self.assertEqual(local_links(self.root, doc), [])
        self.assertEqual(anchors(doc.read_text()), {'real'})

    def test_reference_links_and_undefined_reference(self):
        self.write('docs/guide.md', '# Guide\n')
        doc = self.write('README.md', '[label][Guide]\n[Guide][]\n[Guide]: docs/guide.md "Title"\n[bad][unknown]\n')
        self.assertEqual(local_links(self.root, doc), ['README.md:4: undefined reference [unknown]'])

    def test_reference_destination_is_checked(self):
        doc = self.write('README.md', '[label][target]\n[target]: missing.md\n')
        self.assertEqual(local_links(self.root, doc), ['README.md:2: missing destination: missing.md'])

    def test_nested_relative_paths_and_quoted_title(self):
        self.write('README.md', '# Root\n')
        doc = self.write('docs/guide.md', '[home](../README.md "Home")\n')
        self.assertEqual(local_links(self.root, doc), [])

    def test_external_links_are_offline(self):
        doc = self.write('README.md', '[web](https://example.invalid/a#b)\n[mail](mailto:someone@example.invalid)\n[cdn](//example.invalid/a)\n')
        self.assertEqual(local_links(self.root, doc), [])

    def test_repository_escape_and_absolute_path_are_rejected(self):
        doc = self.write('README.md', '[escape](../outside.md)\n[absolute](/etc/passwd)\n')
        issues = local_links(self.root, doc)
        self.assertEqual(len(issues), 2)
        self.assertIn('escapes repository', issues[0])
        self.assertIn('relative repository path', issues[1])

    def test_unclosed_fence_is_an_error(self):
        doc = self.write('README.md', '# Root\n```text\nunfinished\n')
        self.assertIn('unclosed fenced code block', local_links(self.root, doc)[0])

    def test_missing_structure_and_curriculum_sections_are_detected(self):
        self.write('docs/curriculum.md', '## Month 1 — Incomplete\n### Learning objectives\n')
        self.write('projects/image-classification/README.md', '# Incomplete project\n')
        issues = structure_issues(self.root)
        self.assertIn('missing required file: LICENSE', issues)
        self.assertIn('docs/curriculum.md: expected Months 1–12 exactly once in order', issues)
        self.assertIn('docs/curriculum.md: Month 1 missing section: Assessment criteria', issues)
        self.assertIn('projects/image-classification/README.md: missing section: Testing strategy', issues)


if __name__ == '__main__':
    unittest.main()
