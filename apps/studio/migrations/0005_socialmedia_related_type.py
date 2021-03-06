# Generated by Django 3.2 on 2021-05-26 08:49

import apps.studio.models
from django.db import migrations
import django_enumfield.db.fields


class Migration(migrations.Migration):

    dependencies = [("studio", "0004_people_profile_image")]

    operations = [
        migrations.AddField(
            model_name="socialmedia",
            name="related_type",
            field=django_enumfield.db.fields.EnumField(
                blank=True, enum=apps.studio.models.SocialMedia.RelatedType, null=True
            ),
        )
    ]
