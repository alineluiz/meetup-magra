# Generated by Django 2.2.14 on 2020-07-16 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0004_auto_20200716_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='event_date',
        ),
    ]
