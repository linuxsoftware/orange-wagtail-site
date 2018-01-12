# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 00:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageHighlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=80, verbose_name='Title')),
                ('blurb', wagtail.wagtailcore.fields.RichTextField(blank=True, default='')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, default='', help_text='An area of text for whatever you like'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='welcome',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, default='', help_text='A short introductory message'),
        ),
        migrations.AddField(
            model_name='homepagehighlight',
            name='homepage',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='highlights', to='home.HomePage'),
        ),
        migrations.AddField(
            model_name='homepagehighlight',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page'),
        ),
    ]
