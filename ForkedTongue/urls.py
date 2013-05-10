from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tastypie.api import Api
from ForkedTongue import settings
from torrents.views import TorrentResource, CategoryResource

admin.autodiscover()

torrent_resource = TorrentResource()

v1_api = Api(api_name="v1")
v1_api.register(TorrentResource())
v1_api.register(CategoryResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ForkedTongue.views.home', name='home'),
    url(r'', include('website.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Version 1 API
    (r'^api/', include(v1_api.urls)),


)

urlpatterns += staticfiles_urlpatterns()