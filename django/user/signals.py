from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete
from django.contrib.auth.models import User
from django.conf import settings
from user.models import Key
from internal import utils
import os

@receiver(post_save, sender=User, dispatch_uid='user_post_save')
def user_post_save(sender, instance, **kwargs):
    # create user directory
    path = os.path.join(settings.USER_ROOT, unicode(instance.pk))
    utils.make_directory(path)

    # delete existing links to user directory
    utils.unlink(path, settings.GIT_ROOT)

    # create link to user directory
    if instance.username:
        utils.link(path, os.path.join(settings.GIT_ROOT, instance.username).encode('utf8'))

@receiver(pre_delete, sender=User, dispatch_uid='user_pre_delete')
def user_pre_delete(sender, instance, **kwargs):
    path = os.path.join(settings.USER_ROOT, unicode(instance.pk))
    utils.unlink(path, settings.GIT_ROOT)
    utils.remove_directory(path)

@receiver(pre_save, sender=Key, dispatch_uid='key_pre_save')
def key_pre_save(sender, instance, **kwargs):
    instance.fingerprint = utils.fingerprint(instance.public_key)
