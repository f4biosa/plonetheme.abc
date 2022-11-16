# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plonetheme.abc.testing import PLONETHEME_ABC_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.abc is properly installed."""

    layer = PLONETHEME_ABC_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.abc is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.abc'))

    def test_browserlayer(self):
        """Test that IPlonethemeAbcLayer is registered."""
        from plonetheme.abc.interfaces import (
            IPlonethemeAbcLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeAbcLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_ABC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.abc'])

    def test_product_uninstalled(self):
        """Test if plonetheme.abc is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.abc'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeAbcLayer is removed."""
        from plonetheme.abc.interfaces import \
            IPlonethemeAbcLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeAbcLayer, utils.registered_layers())
