# Generated by Django 4.0.4 on 2022-05-30 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0007_service_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='preco',
            field=models.FloatField(verbose_name='Preço R$'),
        ),
    ]