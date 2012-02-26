#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

"""
Extracts the reStructuredText formatted module documentation block from the
given Python module.

This can then be piped into a ``README.rst`` for instance.
"""

import sys

__docformat__ = "restructuredtext en"

def main():
    mod = __import__(sys.argv[1])
    print mod.__doc__

if __name__ == '__main__':
    main()
