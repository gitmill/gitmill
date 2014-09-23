from django.conf import settings
from django.http import HttpResponseBadRequest
from functools import wraps
import logging
import urlparse

def git_http_backend_view(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # validate parameters
        method = request.META.get('HTTP_METHOD', request.GET.get('method', ''))
        uri = request.META.get('HTTP_URI', request.GET.get('uri', ''))
        if method not in ['GET', 'POST']:
            return HttpResponseBadRequest()
        if not uri or not uri.startswith('/' + settings.PREFIX):
            return HttpResponseBadRequest()
        uri = uri[len('/' + settings.PREFIX):]

        # parse uri
        url = urlparse.urlparse(uri)
        query = urlparse.parse_qs(url.query)
        parts = url.path.split('/')
        if len(parts) < 3:
            return HttpResponseBadRequest()

        # figure out username and name
        username, name = parts[0], parts[1]
        if not name.endswith('.git'):
            return HttpResponseBadRequest()
        name = name.rsplit('.', 1)[0]

        # determine if it is a write request
        access = 'read'
        if parts[-1] == 'git-receive-pack' or 'git-receive-pack' in query.get('service', []):
            access = 'write'

        logging.warn('git: username = %s, name = %s, access = %s, method = %s, uri = %s' % (username, name, access, method, uri))

        kwargs['username'] = username
        kwargs['name'] = name
        kwargs['access'] = access
        return func(request, *args, **kwargs)
    return wrapper
