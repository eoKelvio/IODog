# Generated by Django 4.2.5 on 2023-11-24 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_feedtimes_feed_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedtimes',
            name='feed_time',
            field=models.ManyToManyField(related_name='feed_time', to='api.hours'),
        ),
    ]
