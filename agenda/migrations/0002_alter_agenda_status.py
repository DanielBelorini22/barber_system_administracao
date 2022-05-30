# Generated by Django 4.0.4 on 2022-05-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='status',
            field=models.CharField(blank=True, choices=[('A', 'Agendado'), ('F', 'Finalizado'), ('C', 'Cancelado')], max_length=1, null=True, verbose_name='Status'),
        ),
    ]
