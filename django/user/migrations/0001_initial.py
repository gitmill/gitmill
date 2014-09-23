# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='name', blank=True)),
                ('fingerprint', models.CharField(verbose_name='fingerprint', unique=True, max_length=47, editable=False, validators=[django.core.validators.RegexValidator(regex=b'^([0-9a-f]{2}:){15}[0-9a-f]{2}$')])),
                ('public_key', models.TextField(verbose_name='public key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('user', models.ForeignKey(related_name=b'keys', verbose_name='user', to=settings.AUTH_USER_MODEL, help_text='Owner of the key.')),
            ],
            options={
                'verbose_name': 'key',
                'verbose_name_plural': 'keys',
            },
            bases=(models.Model,),
        ),
    ]
