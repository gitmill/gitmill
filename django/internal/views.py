from django.http import HttpResponse, HttpResponseForbidden
from user.decorators import user_view, key_view, authenticated_view
from repository.decorators import repository_view
from user.models import Key
from internal.decorators import git_http_backend_view

@authenticated_view
@git_http_backend_view
@user_view
@repository_view
def auth(request, access, user, repository, **kwargs):
    granted = False
    if access == 'write' and repository.can_write(request.user):
        granted = True
    if access == 'read' and repository.can_read(request.user):
        granted = True

    if not granted:
        return HttpResponseForbidden()

    response = HttpResponse()
    response['User'] = 'anonymous'
    if request.user:
        response['User'] = request.user.username
    return response

def keys(request):
    """
    command="gitmill-serve <key-id>",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty <public-key>
    """

    def enumerate():
        for key in Key.objects.prefetch_related('user').all():
            yield 'command="gitmill-serve %d",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty %s' % (
                key.id,
                key.public_key,
            )

    return HttpResponse(enumerate())

@key_view
@user_view
@repository_view
def key(request, key, access, user, repository, **kwargs):
    granted = False
    if access == 'write' and repository.can_write(key.user):
        granted = True
    if access == 'read' and repository.can_read(key.user):
        granted = True

    if not granted:
        return HttpResponseForbidden()
    return HttpResponse()
