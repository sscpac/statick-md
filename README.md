# Statick Markdown Plugins

![Unit Tests](https://github.com/sscpac/statick-md/workflows/Unit%20Tests/badge.svg)
[![PyPI version](https://badge.fury.io/py/statick-md.svg)](https://badge.fury.io/py/statick-md)
[![Codecov](https://codecov.io/gh/sscpac/statick-md/branch/master/graph/badge.svg)](https://codecov.io/gh/sscpac/statick-md)
![Python Versions](https://img.shields.io/pypi/pyversions/statick-md.svg)
![License](https://img.shields.io/pypi/l/statick-md.svg)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
![Daily Downloads](https://img.shields.io/pypi/dd/statick-md.svg)
![Weekly Downloads](https://img.shields.io/pypi/dw/statick-md.svg)
![Monthly Downloads](https://img.shields.io/pypi/dm/statick-md.svg)

This is a set of plugins for [Statick](https://github.com/sscpac/statick) that will discover Markdown (md)
files and perform static analysis on those files.

The current plugins will discover Markdown files in a project and can be configured to check those files using

- [markdownlint](https://github.com/DavidAnson/markdownlint)

Custom exceptions can be applied the same way they are with
[Statick exceptions](https://github.com/sscpac/statick/blob/master/GUIDE.md#exceptionsyaml).

## Installation

The recommended method to install these Statick plugins is via pip:

```shell
python3 -m pip install statick-md
```

You can also clone the repository and use it locally.

## Usage

Make sure you install all the dependencies from apt/npm:

```shell
cat install.txt | xargs sudo apt-get install -y
cat npm-deps.txt | xargs sudo npm install -g
```

### Dependency Versions

Markdownlint-cli has occasionally changed defaults via an upgrade that results in lots of new warnings.
To mitigate this you can pin the version of markdownlint-cli in npm-deps.txt by changing `markdownlint-cli` to `markdownlint-cli@0.19`.

### Pip Install

The most common usage is to use statick and statick-md from pip.
In that case your directory structure will look like the following:

- doc
  - md-project
  - statick-output

To run with the default configuration for the statick-md tools use:

```shell
statick md-project/ --output-directory statick-output/ --profile md-profile.yaml
```

### Pip Install and Custom Configuration

There are times when you will want to have a custom Statick configuration.
This is usually done to run a different set of tools than are called out in the default profile, or to add exceptions.
For this case you will have to add the new Statick configuration somewhere.
This example will have custom exceptions in the md-project, such that the directory structure is:

- doc
  - md-project
    - statick-config
      - rsc
        - exceptions.yaml
  - statick-output

For this setup you will run the following:

```shell
statick md-project/ --output-directory statick-output/ --user-paths md-project/statick-config/ --profile md-profile.yaml
```

### Source Install and Custom Configuration

The last type of setup will be to have all of the tools available from cloning repositories, not installing from pip.
The directory structure will look like:

- doc
  - md-project
    - statick-config
      - rsc
        - exceptions.yaml
  - statick-output
  - statick
  - statick-md

Using the example where we want to override the default exceptions with
custom ones in the md-project, the command to run would be:

```shell
./statick/statick md-project/ --output-directory statick-output/ --user-paths statick-md/,md-project/statick-config/ --profile md-profile.yaml
```

## Tests and Contributing

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
python3 -m pip install mypy
mkdir report
mypy --ignore-missing-imports --strict --html-report report/ --txt-report report src
```

It is hoped that in the future we will generate coverage reports from mypy and use those to check for regressions.

### Formatting

Statick code is formatted using [black](https://github.com/psf/black).
To fix locally use

```shell
python3 -m pip install black
black src tests
```
