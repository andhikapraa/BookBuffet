# Generated by Django 4.2.6 on 2023-10-27 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0002_publish_date_added_publish_is_valid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publish',
            name='date_added',
        ),
    ]
