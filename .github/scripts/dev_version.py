#!/usr/bin/env python3
"""
TEST: make the pyecrad version a development version <VERSION>.dev<N>
(used by the pyecrad_wheels workflow, with N the workflow run number).

The version is read from the VERSION file, which is also used by CMake and
must not be modified: the suffix is added through the 'result' template of
the scikit-build-core regex version provider in pyproject.toml.

Usage: dev_version.py N
"""

import sys

PATH = 'pyproject.toml'
LINE = "regex = '(?P<value>\\S+)'\n"

with open(PATH, encoding='utf-8') as f:
    content = f.read()
assert content.count(LINE) == 1, 'version regex not found in pyproject.toml'
content = content.replace(LINE, LINE + f'result = "{{value}}.dev{int(sys.argv[1])}"\n')
with open(PATH, 'w', encoding='utf-8') as f:
    f.write(content)
