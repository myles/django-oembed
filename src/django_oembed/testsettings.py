DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/django-oembed.db'
INSTALLED_APPS = ['oembed',]
#ROOT_URLCONF = ['oembed.url',]
OEMBED_ENDPOINTS = [
    ('http://www.flickr.com/services/oembed', ['http://*.flickr.com/*']),
    ('http://lab.viddler.com/services/oembed/', ['http://*.viddler.com/*']),
    ('http://qik.com/api/oembed.json', ['http://qik.com/video/*', 'http://qik.com/*']),
    ('http://revision3.com/api/oembed/', ['http://*.revision3.com/*']),
    ('http://www.hulu.com/api/oembed.json', ['http://www.hulu.com/watch/*']),
    ('http://www.vimeo.com/api/oembed.json', ['http://www.vimeo.com/*',
        'http://www.vimeo.com/groups/*/*']),
    ('http://oohembed.com/oohembed/', ['http://*.5min.com/Video/*', 
        'http://*.amazon.(com|co.uk|ca)/*/(gp/product|o/ASIN|obidos/ASIN|dp)/*',
        'http://*.collegehumor.com/video:*',
        'http://*.thedailyshow.com/video/*',
        'http://*.flickr.com/photos/*',
        'http://*.funnyordie.com/videos/*', 
        'http://video.google.com/videoplay?*',
        'http://www.hulu.com/watch/*',
        'http://*.imdb.com/title/tt*/',
        'http://*.metacafe.com/watch/*',
        'http://*.nfb.ca/film/*',
        'http://qik.com/*',
        'http://*.revision3.com/*',
        'http://*.slideshare.net/*',
        'http://*.twitpic.com/*',
        'http://twitter.com/*/statuses/*',
        'http://*.viddler.com/explore/*',
        'http://www.vimeo.com/*',
        'http://www.vimeo.com/groups/*/videos/*',
        'http://*.wikipedia.org/wiki/*',
        'http://*.wordpress.com/yyyy/mm/dd/*',
        'http://*.youtube.com/watch*'])
]