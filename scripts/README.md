# Documentation automation

Run from the repository root using Python 3.12 or later:

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

`check_docs.py` checks the required repository/course/project files, all twelve monthly section sets, project specification sections, and local Markdown destinations. It exits nonzero and prints actionable file/line diagnostics when a check fails. It can also check another checkout with `--root /path/to/checkout`.

Supported links are ordinary inline links/images (including angle-bracket paths and optional quoted titles), explicit reference links, collapsed reference links, and reference definitions. It checks percent-encoded relative paths and fragments against ordinary ATX heading slugs, including duplicate heading suffixes. Fenced code and inline code are excluded; unclosed fences fail validation.

This is a repository-specific validator, not a complete Markdown parser/style linter. Shortcut references, HTML anchors/links, setext headings, escaped/nested brackets, and filenames containing literal parentheses are outside its supported syntax. Use simple descriptive filenames and the documented link forms. External URLs, URI schemes, and protocol-relative links are not fetched. Review them using the [resource register](../docs/resources.md).

Regression tests exercise broken/valid paths, spaces/encoded names, heading fragments, references, ignored examples, boundary escapes, and missing structural content. No GPU, network, ROS, package installation, or secret is needed.
