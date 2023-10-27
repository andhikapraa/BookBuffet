# Generated by Django 4.2.6 on 2023-10-27 05:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0003_remove_publish_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='publish',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
