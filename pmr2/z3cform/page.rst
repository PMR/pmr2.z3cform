Page
====

These were just simple rendering pages meant for wrapping by the layout
classes to be replaced by more standard Plone way of rendering 
templates.

Let's subclass one::

    >>> from pmr2.z3cform.tests.base import TestRequest
    >>> from pmr2.z3cform.page import SimplePage
    >>>
    >>> class TestPage(SimplePage):
    ...     template = lambda x: 'Hello'

Then render it::

    >>> context = self.portal
    >>> request = TestRequest()
    >>> page = TestPage(context, request)
    >>> print page()
    <h1 class="documentFirstHeading">Plone site</h1>
    <div id="content-core">
      <div>Hello</div>
    </div>

If we register this view on the main site, we should be able to render
this using the testbrowser.  This will then render the same page with
all the templates associated with Plone::

    >>> import zope.component
    >>> from Testing.testbrowser import Browser
    >>> zope.component.provideAdapter(TestPage, (None, None),
    ...     zope.publisher.interfaces.browser.IBrowserView,
    ...     name='pmr2z3cform-testpage')
    ... 
    >>> tb = Browser()
    >>> tb.open(context.absolute_url() + '/@@pmr2z3cform-testpage')
    >>> 'Plone - http://plone.org' in tb.contents
    True
    >>> '<div>Hello</div>' in tb.contents
    True

As traversal views are generally implementation specific, currently 
testing is deferred to those specific use cases until a more general
pattern is derived.
