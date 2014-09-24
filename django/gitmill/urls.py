from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^' + settings.PREFIX + 'admin/', include(admin.site.urls)),
    url(r'^' + settings.PREFIX + '~/', include('internal.urls', namespace='internal')),

    url(r'^' + settings.PREFIX + 'api/', include('user.apis')),
    url(r'^' + settings.PREFIX + 'api/', include('repository.apis')),

    url(r'^' + settings.PREFIX, include('web.urls', namespace='web')),
    url(r'^' + settings.PREFIX, include('user.urls', namespace='user')),
    url(r'^' + settings.PREFIX, include('repository.urls', namespace='repository')),
)
