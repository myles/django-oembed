from django.conf import settings

OEMBED_ENDPOINTS = getattr(settings, 'OEMBED_ENDPOINTS', None)