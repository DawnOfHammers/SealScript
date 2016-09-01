# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('home', '0006_auto_20160831_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='logo',
        ),
        migrations.AddField(
            model_name='homepage',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.DeleteModel(
            name='Header',
        ),
    ]
