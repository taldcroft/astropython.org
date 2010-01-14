import os
import logging
import StringIO

LOG_STREAM = StringIO.StringIO()

APP_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# If we're debugging, turn the cache off, etc.
# Set to true if we want to have our webapp print stack traces, etc
try:
    DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')
except KeyError:
    DEBUG = True
logging.info("Starting application in DEBUG mode: %s", DEBUG)

# Don't change default_blog or default_page to prevent conflicts when merging #  Bloog source code updates.
# Do change blog or page dictionaries at the bottom of this config module.

BLOG = {
    "bloog_version": "0.8",
    "html_type": "text/html",
    "charset": "utf-8",
    "title": "Astropython",
    "author": "Astropython Contributor",
    # This must be the email address of a registered administrator for the 
    # application due to mail api restrictions.
    "email": "aldcroft@astropython.org",
    "description": "A python resource for astronomers.",
    "root_url": "http://www.astropython.org",
    "master_atom_url": "/feeds/atom.xml",
    # By default, visitors can comment on article for this many days.
    # This can be overridden by setting article.allow_comments
    "days_can_comment": 60,
    # You can override this default for each page through a handler's call to 
    #  view.ViewPage(cache_time=...)
    "cache_time": 3600,

    # Use the default YUI-based theme.
    # If another string is used besides 'default', calls to static files and
    #  use of template files in /views will go to directory by that name.
    "theme": ["default"],
    
    # Display gravatars alongside user comments?
    "use_gravatars": False,
    
    # Do you want to be emailed when new comments are posted?
    "send_comment_notification": False,

    # If you want to use legacy ID mapping for your former blog platform,
    # define it here and insert the necessary mapping code in the
    # legacy_id_mapping() function in ArticleHandler (blog.py).
    # Currently only "Drupal" is supported.
    "legacy_blog_software": None,
    #"legacy_blog_software": "Drupal",
    #"legacy_blog_software": "Serendipity",
    
    # If you want imported legacy entries _not_ mapped in the file above to
    # redirect to their new permanent URL rather than responding on their
    # old URL, set this flag to True.
    "legacy_entry_redirect": False,
}

if DEBUG:
    BLOG['cache_time'] = 0

PAGE = {
    "title": BLOG["title"],
    "articles_per_page": 5,
    "navlinks": [
        { "title": "Forum", 
          "description": "News and views", 
          "url": "/blogs"},
        { "title": "Resources", 
          "description": "Useful links", 
          "url": "/resources"},
        { "title": "Tutorials", 
          "description": "and HowTo's", 
          "url": "/tutorials"},
        { "title": "Snippets", 
          "description": "Bits of code ", 
          "url": "/snippets"},
        { "title": "Contact", 
          "description": "Send us a note", 
          "url": "/contact"},
    ],
    "featuredMyPages": {
        "title": "Featured resources",
        "description": "",
        "entries": [
            { "title": "Python", 
              "url": "http://python.org", 
              "description": "Home page" },
            { "title": "Numpy", 
              "url": "/resource/2009/10/NumPy", 
              "description": "Core numerical libraries" },
            { "title": "Scipy", 
              "url": "/resource/2010/1/SciPy", 
              "description": "Scientific tools for Python" },
            { "title": "Matplotlib", 
              "url": "/resource/2009/11/Matplotlib", 
              "description": "Python 2D plotting library" },
            { "title": "ATpy", 
              "url": "/resource/2009/11/ATpy", 
              "description": "Astronomical tables in Python" },
            { "title": "APLpy", 
              "url": "/resource/2009/10/APLpy", 
              "description": "Hi-quality imaging data plots" },
            { "title": "Sherpa", 
              "url": "/resource/2009/10/CIAO", 
              "description": "Data modeling and fitting" },
        ]
    },
    'categories': {
        'blog': {'default_sort': '-updated',
                 'title': 'Forum',
                 'subtitle': 'announcements, discussions, digressions'},
        'resource': {'default_sort': 'title_lower',
                 'title': 'Resources',
                 'subtitle': 'for the discerning python astronomer',},
        'tutorial': {'default_sort': 'title_lower',
                 'title': 'Tutorials',
                 'subtitle': 'for the learning python astronomer',},
        'snippet': {'default_sort': 'title_lower',
                 'title': 'Snippets',
                 'subtitle': 'for bits of code without a home'},
        }
}
