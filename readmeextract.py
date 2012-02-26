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
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python readmeextract.py module\n")

    # Import the given module
    mod = __import__(sys.argv[1])

    # Print the stipped docstring
    print mod.__doc__.strip()

    # Check whether there is a ``__docformat__`` set.
    try:
        if not mod.__docformat__.startswith("restructuredtext"):
            sys.stderr.write("-> This is probably no reST\n")
    except AttributeError:
        sys.stderr.write("-> Not sure if that is really reST\n")

if __name__ == '__main__':
    main()
