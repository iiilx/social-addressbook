from django.conf.urls.defaults import *

urlpatterns = patterns('social-addressbook.main.views',
    url(r'^$', 'index', name='index'),
)
