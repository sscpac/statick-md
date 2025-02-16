# Statick Markdown Plugins

![Unit Tests](https://github.com/sscpac/statick-md/workflows/Unit%20Tests/badge.svg)
[![PyPI version](https://badge.fury.io/py/statick-md.svg)](https://badge.fury.io/py/statick-md)
[![Codecov](https://codecov.io/gh/sscpac/statick-md/branch/main/graph/badge.svg)](https://codecov.io/gh/sscpac/statick-md)
![Python Versions](https://img.shields.io/pypi/pyversions/statick-md.svg)
![License](https://img.shields.io/pypi/l/statick-md.svg)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
![Daily Downloads](https://img.shields.io/pypi/dd/statick-md.svg)
![Weekly Downloads](https://img.shields.io/pypi/dw/statick-md.svg)
![Monthly Downloads](https://img.shields.io/pypi/dm/statick-md.svg)

This is a set of plugins for [Statick](https://github.com/sscpac/statick) that will discover documentation related files
and perform static analysis on those files.

Custom exceptions can be applied the same way they are with
[Statick exceptions](https://github.com/sscpac/statick/blob/master/GUIDE.md#exceptionsyaml).

## Table of Contents

- [Statick Markdown Plugins](#statick-markdown-plugins)
  - [Table of Contents](#table-of-contents)
  - [Deprecated](#deprecated)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Dependency Versions](#dependency-versions)
    - [Pip Install](#pip-install)
    - [Pip Install and Custom Configuration](#pip-install-and-custom-configuration)
  - [Existing Plugins](#existing-plugins)
    - [Discovery Plugins](#discovery-plugins)
    - [Tool Plugins](#tool-plugins)
  - [Contributing](#contributing)
    - [Mypy](#mypy)
    - [Formatting](#formatting)

## Deprecated

This set of plugins was merged into the main [Statick] repository and Python package.
All future development will happen in that repository.

## Installation

The recommended method to install these Statick plugins is via pip:

```shell
pip install statick-md
```

You can also clone the repository and use it locally.

## Usage

Make sure you install all the dependencies from apt/npm.
See <https://github.com/nodesource/distributions> for Node/npm installation instructions.

Configure npm to allow a non-root user to install packages.

```shell
npm config set prefix '~/.local/'
```

Make sure `~/.local/bin` exists.
Check your `PATH` with `echo $PATH`.
If `~/.local/bin` is not listed then add it to your `PATH`.

```shell
mkdir -p ~/.local/bin
echo 'export PATH="$HOME/.local/bin/:$PATH"' >> ~/.bashrc
```

Install packages.

```shell
npm install -g markdownlint-cli
npm install -g write-good
```

### Dependency Versions

Markdownlint-cli has occasionally changed defaults via an upgrade that results in lots of new warnings.
To mitigate this you can pin the version of markdownlint-cli when installing by changing `markdownlint-cli` to `markdownlint-cli@0.19`.

### Pip Install

The most common usage is to use statick and statick-md from pip.
In that case your directory structure will look like the following:

```shell
project-root
 |- md-project
```

To run with the default configuration for the statick-md tools use:

```shell
statick md-project/ -o /tmp/statick-output/ --level md --log info
```

### Pip Install and Custom Configuration

There are times when you will want to have a custom Statick configuration.
This is usually done to run a different set of tools than are called out in the default profile, or to add exceptions.
For this case you will have to add the new Statick configuration somewhere.
This example will have custom exceptions in the md-project, such that the directory structure is:

```shell
project-root
|- md-project
    |- statick-config
        |- rsc
            |- exceptions.yaml
```

For this setup you will run the following:

```shell
statick md-project/ --o /tmp/statick-output/ -u md-project/statick-config/ --level md
```

## Existing Plugins

### Discovery Plugins

File Type | Extensions
:-------- | :---------
markdown         | `.md`
reStructuredText | `.rst`

### Tool Plugins

Tool | About
:--- | :----
[markdownlint][markdownlint] | A Node.js style checker and lint tool for Markdown/CommonMark files.
[rstcheck][rstcheck]         | Checks syntax of reStructuredText and code blocks nested within it.
[rst-lint][rst-lint]         | Checks syntax of reStructuredText and code blocks nested within it.
[write-good]                 | Naive linter for English prose.

## Contributing

If you write a new feature for Statick or are fixing a bug,
you are strongly encouraged to add unit tests for your contribution.
In particular, it is much easier to test whether a bug is fixed (and identify
future regressions) if you can add a small unit test which replicates the bug.

Before submitting a change, please run tox to check that you have not
introduced any regressions or violated any code style guidelines.

### Mypy

Statick Markdown uses [mypy](http://mypy-lang.org/) to check that type hints are being followed properly.
Type hints are described in [PEP 484](https://www.python.org/dev/peps/pep-0484/) and allow for static typing in Python.
To determine if proper types are being used in Statick Markdown the following command will show any errors, and create several
types of reports that can be viewed with a text editor or web browser.

```shell
pip install mypy
mkdir report
mypy --ignore-missing-imports --strict src
```

### Formatting

Statick code is formatted using [black](https://github.com/psf/black).
To fix locally use

```shell
pip install black
black src tests
```

[markdownlint]: https://github.com/igorshubovych/markdownlint-cli
[rstcheck]: https://github.com/myint/rstcheck
[rst-lint]: https://github.com/twolfson/restructuredtext-lint
[write-good]: https://github.com/btford/write-good
[Statick]: https://github.com/sscpac/statick
