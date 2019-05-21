# Generated by Django 2.2.1 on 2019-05-18 09:56

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagsDemoPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('welcome', wagtail.core.fields.RichTextField(blank=True, default='', help_text='A welcome message')),
                ('content', wagtail.core.fields.RichTextField(blank=True, default='', help_text='An area of text for whatever you like')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]