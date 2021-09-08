# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## Unreleased

### Added

### Fixed

### Removed

## v0.0.9 - 2021-09-08

### Added

- [proselint](https://github.com/amperser/proselint) tool plugin and tests. (Thomas Denewiler, @tdenewiler, #38, #39)
- [write-good](https://github.com/btford/write-good) tool plugin and tests. (Thomas Denewiler, @tdenewiler, #41)
- reStructuredText discovery plugin and tests.
- [rstcheck](https://github.com/myint/rstcheck) tool plugin and tests.
- [rst-lint](https://github.com/twolfson/restructuredtext-lint) tool plugin and tests.

### Fixed

- Specifying an encoding when calling open (pylint: [W1514](https://pylint.pycqa.org/en/latest/technical_reference/features.html)).

### Removed

## v0.0.8 - 2021-05-28

### Changed

- Switch type hints from comment style to inline style.
- Renaming plugin directories to match Statick's directory structure.
- Upgraded version of markdownlint-cli used in Actions to the latest available.
- For testing with Actions, the installed version of Node was upgraded from v10 to v14.
  Node v10 is no longer supported.
  Node v14 is recommended by the developers as it is a long-term support (LTS) release.

### Removed

- Remove testing support for Ubuntu 16.04 and Python 3.5.
  There is no guarantee Statick will work in those environments any longer.

## v0.0.7 - 2021-01-22

This is expected to be the final release that supports Python 3.5.
Ubuntu 16.04 has reached end-of-life status.
The final release of ROS Kinetic has been made.
See <https://github.com/sscpac/statick/discussions/290> for a discussion on Python 3.5 support in Statick.

### Changed

- Turned off line length checks for Markdown code blocks.

### Added

- Using type hints as introduced in Python 3.5 and improved in Python 3.6.
  Type hints are described in [PEP 438](https://www.python.org/dev/peps/pep-0483/)
  and [PEP 484](https://www.python.org/dev/peps/pep-0484/).
  They provide static typing for methods and variables.
  The use of mypy is encouraged to look for errors in expected types.

### Removed

- No longer supporting pypy3 due to issues with type hints and mypy.

## v0.0.6 - 2021-01-19

### Changed

- Convert use of print() and show tool output flags to the built-in Python logging module. (Thomas Denewiler, @tdenewiler)

## v0.0.5 - 2020-12-22

### Added

- Take advantange of new `DiscoveryPlugin.find_files` function that only walks a package's path once instead of
  in each discovery plugin.
  This should lead to a speed improvement in the discovery phase. (Alexander Xydes, @xydesa)

## v0.0.4 - 2020-04-06

### Fixed

- Fixed installation of config and profile files from this package.

## v0.0.3 - 2020-04-06

### Added

- Installing .markdownlintrc file with this package.
- Formatted all code using black. Added Github Action to ensure future commits are consistent with black formatting.
- Using markdownlint statick plugin to check documentation files.

### Changed

- Switched from travis ci to github actions.

### Fixed

- Limit discovery plugins to only markdown files in md config levels. (Thomas Denewiler, @tdenewiler)

## v0.0.2 - 2020-02-14

### Added

- Adding support for markdownlint output with column number (Alexander Xydes, @axydes)

## v0.0.1 - 2020-02-13

### Added

- Initial release (Alexander Xydes, @axydes)
