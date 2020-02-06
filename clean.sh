#!/bin/bash

rm -rf build/ dist/ .tox/ output-py* */*.egg-info *.egg-info statick_output/* *.log
find . -name "*.pyc" -type f -delete
find . -depth -name __pycache__ -type d -exec rm -r {} +
