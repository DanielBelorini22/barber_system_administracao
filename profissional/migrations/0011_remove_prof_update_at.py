# Generated by Django 4.0.4 on 2022-06-21 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0010_prof_created_at_prof_update_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prof',
            name='update_at',
        ),
    ]