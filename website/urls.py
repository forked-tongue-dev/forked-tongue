from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.index', name='index'),
    url(r'^login/$', 'website.views.login', name="login"),
    url(r'^mirror/$', 'website.views.select_mirror', name='random_mirror'),
    # url(r'^ForkedTongue/', include('ForkedTongue.foo.urls')),


)