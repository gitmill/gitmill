from django.conf.urls import patterns, url

urlpatterns = patterns('user.views',
    url(r'^(?P<username>[A-Za-z0-9_@+.\-]{1,30})$', 'user', name='user'),
)
