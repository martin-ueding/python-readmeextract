from epydoc.markup import epytext

def test():
    """
    Test::

        Indented paragraph

    C{code} and B{bold}
    """
    pass

doc = test.__doc__
print doc

print "---"

dom = epytext.parse_docstring(doc, [])
print dom

print "---"

print dom.to_html(None)
print "---"
print dom.to_plaintext(None)
print "---"
print dom.to_latex(None)
