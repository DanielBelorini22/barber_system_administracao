# Generated by Django 4.0.4 on 2022-06-21 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0014_prof_update_at_alter_prof_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prof',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='prof',
            name='update_at',
        ),
    ]
