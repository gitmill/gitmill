# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of the repository, cannot contain special characters other than hyphens.', max_length=64, verbose_name='name', validators=[django.core.validators.RegexValidator(regex=b'^[^\\x00-\\x2c\\x2f\\x3a-\\x40\\x5b-\\x5e\\x60\\x7b-\\x7f\\s]+$')])),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('is_private', models.BooleanField(default=True, help_text='Restrict read access to specified users and groups.', verbose_name='is private')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('groups', models.ManyToManyField(help_text='Users in these groups have right access to the repository.', to='auth.Group', verbose_name='groups', blank=True)),
                ('user', models.ForeignKey(related_name=b'repositories', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, help_text="Owner of the repository. Repository path will be prefixed by owner's username.", null=True, verbose_name='user')),
                ('users', models.ManyToManyField(help_text='These users have right access to the repository.', to=settings.AUTH_USER_MODEL, verbose_name='users', blank=True)),
            ],
            options={
                'ordering': ['user', 'name'],
                'verbose_name': 'repository',
                'verbose_name_plural': 'repositories',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='repository',
            unique_together=set([('user', 'name')]),
        ),
    ]
