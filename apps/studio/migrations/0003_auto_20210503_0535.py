# Generated by Django 3.2 on 2021-05-03 05:35

import apps.studio.models
from django.db import migrations
import django_enumfield.db.fields


class Migration(migrations.Migration):

    dependencies = [("studio", "0002_people")]

    operations = [
        migrations.AlterModelOptions(
            name="people",
            options={"verbose_name": "People", "verbose_name_plural": "B - People"},
        ),
        migrations.RemoveField(model_name="socialmedia", name="icon"),
        migrations.RemoveField(model_name="socialmedia", name="name"),
        migrations.AddField(
            model_name="socialmedia",
            name="social_media_type",
            field=django_enumfield.db.fields.EnumField(
                blank=True,
                enum=apps.studio.models.SocialMedia.SocialMediaType,
                null=True,
            ),
        ),
    ]
