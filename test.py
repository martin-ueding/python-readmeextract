from epydoc.markup import epytext
from epydoc import docparser
import subprocess

__doc__ = """
Test::

    Indented paragraph

C{code} and B{bold}
"""

print __doc__

def foo():
    pass

if __name__ == '__main__':
    filename = "test.py"

    valuedoc = docparser.parse_docs(filename)

    print valuedoc
    print "---"
    print valuedoc.summary
    print "---"

if False:

    dom = epytext.parse_docstring(valuedoc.docstring, [])
    latex = dom.to_latex(None)

    proc = subprocess.Popen(["pandoc", "-r", "latex", "-w", "markdown"], stdin=subprocess.PIPE)
    proc.stdin.write(latex)
    proc.stdin.close()
    proc.communicate()
