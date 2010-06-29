from django.conf import settings
SLOT_CHOICES = getattr(settings, 'CMSPLUGIN_BANNER_SLOT_CHOICES', ( ('Content-Default','Content-Default'), ))
STYLE_CHOICES = getattr(settings, 'CMSPLUGIN_BANNER_STYLE_CHOICES', ( ('default','default'), ))