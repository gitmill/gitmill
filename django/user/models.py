from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

class Key(models.Model):

    name = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('name'),
    )

    fingerprint = models.CharField(
        unique=True,
        editable=False,
        max_length=47,
        validators=[RegexValidator(regex=r'^([0-9a-f]{2}:){15}[0-9a-f]{2}$')],
        verbose_name=_('fingerprint'),
    )

    public_key = models.TextField(verbose_name=_('public key'))

    user = models.ForeignKey(
        User,
        related_name='keys',
        verbose_name=_('user'),
        help_text=_('Owner of the key.'),
    )

    # meta
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modified'))

    class Meta:
        verbose_name = _('key')
        verbose_name_plural = _('keys')

    def __unicode__(self):
        return self.fingerprint
