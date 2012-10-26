from unittest import TestSuite, makeSuite

from plone.browserlayer.layer import mark_layer
from zope.app.publication.zopepublication import BeforeTraverseEvent

from pmr2.testing.base import TestCase


class TestProductInstall(TestCase):

    def afterSetUp(self):
        self.addProfile('pmr2.z3cform:default')
        event = BeforeTraverseEvent(self.portal, self.portal.REQUEST)
        mark_layer(self.portal, event)

    def testLayerApplied(self):
        from pmr2.z3cform.interfaces import IFormLayer
        self.assertTrue(IFormLayer.providedBy(self.portal.REQUEST))


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    return suite
