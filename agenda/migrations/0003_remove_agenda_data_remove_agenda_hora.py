# Generated by Django 4.0.4 on 2022-06-22 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_agenda_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='data',
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='hora',
        ),
    ]
