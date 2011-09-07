import os
import sys
sys.path.append('/srv/www')
sys.path.append('/srv/www/social-addressbook')

os.environ['DJANGO_SETTINGS_MODULE'] = 'social-addressbook.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


