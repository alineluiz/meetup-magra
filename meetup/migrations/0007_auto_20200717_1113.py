# Generated by Django 2.2.14 on 2020-07-17 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0006_auto_20200717_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id_meetup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='meetup.Meetup'),
        ),
    ]
