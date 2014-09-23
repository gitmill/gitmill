from django.conf.urls import patterns, url

urlpatterns = patterns('internal.views',
    url(r'^$', 'keys', name='keys'),
    url(r'^(?P<id>[0-9]+)/(?P<access>(read|write))/(?P<username>[A-Za-z0-9_@+.\-]{1,30})/(?P<name>[^\x00-\x2c\x2f\x3a-\x40\x5b-\x5e\x60\x7b-\x7f\s]{1,64})/$', 'key', name='key'),
    url(r'^auth/$', 'auth', name='auth'),
)
