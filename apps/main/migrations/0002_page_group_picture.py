# Generated by Django 3.2 on 2021-06-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='group_picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='group_picture'),
        ),
    ]
