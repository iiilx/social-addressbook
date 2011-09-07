from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import redirect_to

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^$', redirect_to, {'url': '/addressbook/'}),
    (r'^addressbook/', include('addressbook.urls')),
    (r'^accounts/', include('socialauth.urls')),
    #url(r'^accounts/', include('registration.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('social-addressbook.main.views',
    url(r'^$', 'index', name='index'),
)
