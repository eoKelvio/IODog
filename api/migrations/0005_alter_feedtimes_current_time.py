# Generated by Django 4.2.5 on 2023-11-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_feed_feedtimes_feed_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedtimes',
            name='current_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
