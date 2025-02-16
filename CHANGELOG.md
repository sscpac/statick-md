# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## v0.4.0 - 2025-02-07

This set of plugins was merged into the main [Statick] repository and Python package.
All future development will happen in that repository.

### Updated

- The Statick dependency was pinned to lower than version 0.12.
  - This will ensure these plugins are not installed in the same space as the main `statick` package.
    Having both packages installed would cause conflicts between plugins.

## v0.3.1 - 2025-01-20

### Added

- Support for Python 3.12 and 3.13.
- Use of `pyproject.toml` instead of `setup.py` and `requirements.txt`.
- Supports new plugin discovery mechanism for the main Statick tool.
  - Switched from yapsy to setuptools for plugin mechanism. (sscpac/statick#508)

### Changed

- Disabled code coverage requirements in CI for now.
  - Unable to get line coverage working with new plugin mechanism.
    Unit tests still work to find problems.
- Updated README to use more modern approach to installing Python and NPM packages.
- Rename plugin modules so they are shorter and less redundant.

### Removed

- No longer support Python 3.8.
- Proselint tool removed.
  - Unable to resolve type hint and unit test issues.
    Tool not used as far as Statick developers are aware.

## v0.2.0 - 2025-01-03

### Removed

- Removed support for Python 3.7.
- Removed use of flake8 for unit tests.

## v0.1.3 - 2023-04-24

### Changed

- Updated publish workflow runner to Ubuntu 22.04 since 18.04 is removed. (#67)

## v0.1.2 - 2023-04-24

Using current fixes of running tools against all files at once instead of one file at a time on the
<https://github.com/github/opensource.guide> repository finds 238 Markdown files and shows significant decrease in
execution time.

```shell
INFO:root:Scanning package opensource.guide (/home/user/src/opensource.guide) at level documentation
INFO:root:---Discovery---
INFO:root:Running markdown discovery plugin...
INFO:root:  299 markdown files found.
INFO:root:  After filtering, 238 markdown files will be scanned.
INFO:root:markdown discovery plugin done.
```

| package          | name             | plugin_type | duration (main) | duration (unreleased) |
| ---------------- | ---------------- | ----------- | --------------- | --------------------- |
| opensource.guide | find files       |  Discovery  | 4.9255          |  4.9149               |
| opensource.guide | markdown         |  Discovery  | 0.0088          |  0.0086               |
| opensource.guide | markdownlint     |    Tool     | 28.0523         |  0.8511               |
| opensource.guide | print_to_console |  Reporting  | 0.4227          |  0.3386               |
| Overall          |                  |             | 34.5287         |  7.2445               |

Testing the `rstcheck` tool plugin against the <https://github.com/PointCloudLibrary/blog> repository shows
improvements for scanning all files at once.
Statick discovered 353 rst files in this repository.

| package  | name             | plugin_type | duration (main) | duration (unreleased) |
| -------- | ---------------- | ----------- | --------------- | --------------------- |
| pcl_blog | find files       | Discovery   | 5.9150          |  5.9158               |
| pcl_blog | markdown         | Discovery   | 0.0033          |  0.0026               |
| pcl_blog | rst              | Discovery   | 0.0090          |  0.0083               |
| pcl_blog | markdownlint     | Tool        | 0.0994          |  0.1017               |
| pcl_blog | rstcheck         | Tool        | 114.8899        |  0.4774               |
| pcl_blog | print_to_console | Reporting   | 0.0021          |  0.0017               |
| Overall  |                  |             | 121.0291        |  6.6186               |

(Note that this testing was done with a local fix in the Statick `exceptions` module for a `UnicodeDecodeError`.
That fix will get pushed to Statick in the future.)

### Added

- Process all source files at once with tools that support passing in a list of files, instead of invoking each tool
  per file. (#63)
- Ubuntu 22.04 used in continuous integration workflows. (#62)
- Python 3.11 used in continuous integration workflows. (#62)

### Changed

- Update GitHub Actions to use latest versions. (#62)

### Fixed

- Ensuring that "Cannot find module" thrown errors from nodejs in markdownlint tool plugin cause statick to error. (#64)

### Removed

- Ubuntu 18.04 removed from continuous integration workflows. (#62)
- Removed deprecated pypi package [codecov](https://github.com/codecov/codecov-python) from Tox configuration. (#)
  Discussion at: <https://community.codecov.com/t/codecov-yanked-from-pypi-all-versions/4259>.

## v0.1.1 - 2022-10-10

### Changed

- Updated usage of `inherits_from` in config file to new list format. (#57, @gregtkogut)
- Pin flake8 version to less than v5 until <https://github.com/tholo/pytest-flake8/issues/87> is fixed. (#58)

## v0.1.0 - 2022-01-04

### Removed

- Drop support for Python 3.6 due to end-of-life of that distribution.
  See <https://endoflife.date/python>.
  To continue using Statick with Python 3.6 [pin the version](https://pip.pypa.io/en/stable/user_guide/)
  used to the `0.0` tags.
  An example is at the discussion at <https://github.com/sscpac/statick/discussions/376>.

## v0.0.10 - 2022-01-04

### Added

- Add Python 3.10 support. (Thomas Denewiler, @tdenewiler, #48)
- Add weekly tests and a manual trigger to the test workflow.
- Switch testing environment from macos-latest to macos-10.15.
  This is to retain support for Python 3.6. (Thomas Denewiler, @tdenewiler, #46)

### Fixed

- Switch use of codecov-action from v1 to v2 for increased stability when uploading reports.
  (Thomas Denewiler, @tdenewiler, #45)
- Use quotes for version numbers in YAML to avoid truncating trailing zeros. (Thomas Denewiler, @tdenewiler, #48)
- Fix proselint tests by changing exclamation point to a period in test Markdown files. (Thomas Denewiler, @tdenewiler, #50)

## v0.0.9 - 2021-09-08

### Added

- [proselint](https://github.com/amperser/proselint) tool plugin and tests. (Thomas Denewiler, @tdenewiler, #38, #39)
- [write-good](https://github.com/btford/write-good) tool plugin and tests. (Thomas Denewiler, @tdenewiler, #41)
- reStructuredText discovery plugin and tests.
- [rstcheck](https://github.com/myint/rstcheck) tool plugin and tests.
- [rst-lint](https://github.com/twolfson/restructuredtext-lint) tool plugin and tests.

### Fixed

- Specifying an encoding when calling open (pylint: [W1514](https://pylint.pycqa.org/en/latest/technical_reference/features.html)).

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
