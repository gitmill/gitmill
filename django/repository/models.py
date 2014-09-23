from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.conf import settings

class Repository(models.Model):
    """
    Git repository
    """

    # basic info
    name = models.CharField(
        max_length=64,
        validators=[RegexValidator(regex=r'^[^\x00-\x2c\x2f\x3a-\x40\x5b-\x5e\x60\x7b-\x7f\s]+$')],
        verbose_name=_('name'),
        help_text=_('Name of the repository, cannot contain special characters other than hyphens.'),
    )

    description = models.TextField(blank=True, verbose_name=_('description'))

    # owner
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='repositories',
        on_delete=models.SET_NULL,
        verbose_name=_('user'),
        help_text=_('Owner of the repository. Repository path will be prefixed by owner\'s username.'),
    )

    # access control
    users = models.ManyToManyField(
        User,
        blank=True,
        verbose_name=_('users'),
        help_text=_('These users have right access to the repository.'),
    )

    groups = models.ManyToManyField(
        Group,
        blank=True,
        verbose_name=_('groups'),
        help_text=_('Users in these groups have right access to the repository.'),
    )

    is_private = models.BooleanField(
        default=True,
        verbose_name=_('is private'),
        help_text=_('Restrict read access to specified users and groups.'),
    )

    # meta
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modified'))

    class Meta:
        verbose_name = _('repository')
        verbose_name_plural = _('repositories')
        ordering = ['user', 'name']
        unique_together = ['user', 'name']

    def __unicode__(self):
        if self.user:
            return u'%s/%s' % (self.user.username, self.name)
        return u'./%s' % (self.name)

    def can_read(self, user):
        if not user and settings.PROTECTED:
            return False
        if not self.is_private:
            return True
        return self.can_write(user)

    def can_write(self, user):
        if not user:
            return False
        if user.id == self.user_id:
            return True
        if self.users.filter(pk=user.id).exists():
            return True
        if self.groups.filter(user__pk=user.id).exists():
            return True
        return False
