# Generated by Django 4.0.4 on 2022-05-30 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0006_service_atualizado_em'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]
