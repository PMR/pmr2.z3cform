Introduction
============

This package extends z3c.form and plone.z3cform for usage within PMR2
and related libraries.  Problems this package attempt to tackle are:

  - Unifying browser class for test and Plone.  It may be possible to
    support other frameworks by registering the root view to the desired
    layer.
  - Offer the same dynamic browser class to standard non-form views.
  - XSS (Cross Site Scripting) prevention via the use of appropriate 
    form authenticators, e.g. plone.protect for Plone.
  - Forms with traversal subpaths.

Installation and usage
----------------------

Just add or modified the `install_requires` option into the setup
function in a typical `setup.py`, like so::

    from setuptools import setup
    
    setup(
        ...
        install_requires=[
            ...
            'pmr2.z3cform',
        ]
    )
