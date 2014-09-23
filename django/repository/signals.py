from __future__ import with_statement
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from repository.models import Repository
from django.conf import settings
from internal import utils
import os

@receiver(post_save, sender=Repository, dispatch_uid='repository_post_save')
def repository_post_save(sender, instance, **kwargs):
    # create bare git repository
    path = os.path.join(settings.REPOSITORY_ROOT, unicode(instance.pk))
    utils.make_directory(path)
    utils.git_init(path)

    # write the description file
    with open(os.path.join(path, 'description'), 'wb') as f:
        f.write(instance.description.encode('utf8') + '\n')

    # delete existing links to repository
    utils.unlink(path, settings.USER_ROOT)

    # when repository attached to a user, link it under the user
    if instance.user:
        utils.link(path, os.path.join(settings.USER_ROOT, unicode(instance.user.pk), instance.name + '.git').encode('utf8'))

@receiver(pre_delete, sender=Repository, dispatch_uid='repository_pre_delete')
def repository_pre_delete(sender, instance, **kwargs):
    path = os.path.join(settings.REPOSITORY_ROOT, unicode(instance.pk))
    utils.unlink(path, settings.USER_ROOT)
    utils.remove_directory(path)
