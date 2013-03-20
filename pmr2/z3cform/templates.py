import os.path

from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from plone.app.z3cform import templates

path = lambda p: os.path.join(os.path.dirname(__file__), 'templates', p)


class PlainMainMacros(templates.Macros):
    """\
    Trying to make life easier for general testing
    """

    index = ViewPageTemplateFile(path('plain-main-macros.pt'))


class PloneMainMacros(templates.Macros):
    """\
    The main macros, including templates.
    """

    index = ViewPageTemplateFile(path('plone-main-macros.pt'))


class PloneZ3cformMacros(templates.Macros):
    """
    Extension to the plone.z3cform macros.

    Implements recursive rendering of subgroups and buttons for them.

    Since this is experimental, it is not enabled.  Users of this macro
    should do so by having it render specific for user specific content,
    or define a layer, and then define the zcml like so::

        <browser:page
            name="ploneform-macros"
            for="my.custom.content.IContent"
            layer="my.custom.interfaces.ILayer"
            class="pmr2.z3cform.templates.Macros"
            allowed_interface="zope.interface.common.mapping.IItemMapping"
            permission="zope.Public"
            />

    """

    index = ViewPageTemplateFile(path('plonez3c-form-macros-ex.pt'))
