from epydoc.markup import epytext
import subprocess

def test():
    """
    Test::

        Indented paragraph

    C{code} and B{bold}
    """
    pass

doc = test.__doc__
dom = epytext.parse_docstring(doc, [])
latex = dom.to_latex(None)

proc = subprocess.Popen(["pandoc", "-r", "latex", "-w", "markdown"], stdin=subprocess.PIPE)
proc.stdin.write(latex)
proc.stdin.close()
proc.communicate()
