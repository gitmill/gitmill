from django.conf.urls import patterns, url

urlpatterns = patterns('repository.views',
    url(r'^(?P<username>[A-Za-z0-9_@+.\-]{1,30})/(?P<name>[^\x00-\x2c\x2f\x3a-\x40\x5b-\x5e\x60\x7b-\x7f\s]{1,64})/$', 'repository', name='repository'),
)

