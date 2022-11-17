# -*- coding: utf-8 -*-
from  plone import api

from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

import os 

@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'plonetheme.abc:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    portal = api.portal.get()
    _create_content(portal)

def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.

def _create_content(portal):
    if not portal.get('slider-images', False):
        slider = api.content.create(
            type='Folder',
            container=portal,
            Title = 'Slider',
            id='slider-images'
        )
    
        for slider_number in range(1, 4):
            slider_name = 'Slider-{0}'.format(str(slider_number))
            slider_image = api.content.create(
                type='Image',
                container = slider,
                title=slider_name,
                id=slider_name
            )
            slider_image.image = _load_image(slider_number)

        api.content.transition(obj=slider, transition='publish')

def _load_image(slider):
    from plone.namedfile.file import NamedBlobImage
    filename = os.path.join(
        os.path.dirname(__file__),
        'theme',
        'img',
        'slide-{0}.jpg'.format(slider),
    )

    return NamedBlobImage(
        data=open(filename, 'rb').read(),
        filename='slide-{0}.jpg'.format(slider)
    )
    
