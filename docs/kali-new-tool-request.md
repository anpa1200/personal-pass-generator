# Kali Linux New Tool Request: Personal Pass Generator

Use this text when submitting under **New Tool Requests** at
<https://bugs.kali.org/>. Set reproducibility to `N/A`, severity to `minor`,
and priority to `normal`.

## Summary

personal-pass-generator - focused personalized password wordlist generator

## Description

[Name] - Personal Pass Generator

[Version] - 1.1.0

[Homepage] - https://github.com/anpa1200/personal-pass-generator

[Download] - https://github.com/anpa1200/personal-pass-generator/releases/tag/v1.1.0

[Author] - Andrey Pautov

[Licence] - GNU General Public License v3.0 or later

[Description] - Personal Pass Generator creates focused password candidate
wordlists for authorized password-security assessments. It supports interactive
and scriptable workflows, case and leet variants, bounded prefix/suffix
mutations, minimum/maximum length filters, and sorted deduplicated output.

[Dependencies] - Python 3.9 or newer; no third-party runtime dependencies.

[Similar tools] - cupp, crunch, john

[Activity] - Actively maintained. The standalone project was released in June
2026 and includes automated tests and GitHub Actions CI.

[How to install] - Download the v1.1.0 source release and run
`python3 -m pip install .`. Debian/Kali package metadata is included in the
`debian/` directory.

[How to use] - Run `ppg` for interactive mode. Example scriptable use:
`ppg --word alice --word acme --leet --min-length 8 --max-length 14 -o candidates.txt`.

[Packaged] - Debian/Kali package metadata is included upstream and builds the
`personal-pass-generator` binary package.

After Kali creates the issue, configure
[status notifications](kali-status-notifications.md).
