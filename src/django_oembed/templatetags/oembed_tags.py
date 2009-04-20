import oembed

from django.template import Library, Node, TemplateSyntaxError
from django.utils.translation import ugettext as _
from django.conf import settings

register = Library()

if settings.OEMBED_ENDPOINTS is None:
    raise TemplateSyntaxError(_('Add some oEmbed endpoints to your settings file.'))

consumer = oembed.OEmbedConsumer()
for url, url_schemas in settings.OEMBED_ENDPOINTS:
    endpoint = oembed.OEmbedEndpoint(url, url_schemas)
    consumer.addEndpoint(endpoint)

class OEmbed(Node):
    def __init__(self, url, context_var):
        self.url = url
        self.context_var = context_var
    
    def render(self, context):
        url = self.url
        if url is None:
            raise TemplateSyntaxError(_('Please provide a URL for oEmbed.'))
        context[self.context_var] = url
        return ''

def do_oembed(parser, token):
    """
    TODO
    
    Usage::
        
        {% oembed [url] as [varname] %}
    
    Examples::
        
        {% oembed 'http://www.flickr.com/photos/wizardbt/2584979382/' as flick_photo %}
    """
    bits = token.contets.split()
    len_bits = len(bits)
    if len_bits not in (4, 6):
        raise TemplateSyntaxError(_("second argument to %s tag must be 'as'") % bits[0])
    return OEmbed(bits[1], bits[3])

register.tag('oembed', do_oembed)