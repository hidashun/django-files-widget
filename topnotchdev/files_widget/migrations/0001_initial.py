# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import topnotchdev.files_widget.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileIcon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('extension', models.CharField(blank=True, null=True, max_length=100)),
                ('image', topnotchdev.files_widget.fields.ImageField(max_length=200)),
                ('display_text_overlay', models.BooleanField(default=True)),
                ('overlay_text', models.CharField(blank=True, null=True, max_length=7, help_text='Leave blank to display file extension')),
                ('base_color', models.CharField(blank=True, null=True, max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IconSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('css_path', models.CharField(blank=True, null=True, max_length=200, help_text='Optional css file for icon styling')),
                ('active', models.BooleanField(default=True)),
                ('priority', models.IntegerField(default=1)),
                ('default_icon', models.ForeignKey(blank=True, to='files_widget.FileIcon', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fileicon',
            name='icon_set',
            field=models.ForeignKey(to='files_widget.IconSet'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='GlobalPermission',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.permission',),
        ),
    ]
