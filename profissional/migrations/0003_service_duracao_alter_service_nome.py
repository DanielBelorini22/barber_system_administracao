# Generated by Django 4.0.4 on 2022-05-30 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profissional', '0002_alter_service_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='duracao',
            field=models.CharField(choices=[('meia_hora', '00:30'), ('uma_hora', '01:00'), ('uma_hora_e_meia', '01:30'), ('duas_horas', '02:00')], default=1, max_length=50, verbose_name='Duração'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='nome',
            field=models.CharField(choices=[('corte', 'Corte de cabelo'), ('barba', 'Barba'), ('sobrancelha', 'Sobrancelha'), ('corte_sobrancelha', 'Corte de cabelo e sobrancelha'), ('corte_barba', 'Corte de cabelo e barba'), ('barba_sobrancelha', 'Barba e sobrancelha'), ('corte_barba_sobrancelha', 'Corte de cabelo, barba e sobrancelha')], max_length=100, verbose_name='Serviço'),
        ),
    ]
