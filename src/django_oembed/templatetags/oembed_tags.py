from django.template import Library, Node, TemplateSyntaxError
from django.utils.translation import ugettext as _

register = Library()

class Oembed(Node):
    def __init__(self, url):
        self.url = url
    
    def render(self, context):
        if url is None:
            raise TemplateSyntaxError(_('Please provide a URL for Oembed.'))
        
        