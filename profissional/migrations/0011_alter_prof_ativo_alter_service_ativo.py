# Generated by Django 4.0.4 on 2022-07-01 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0010_prof_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
