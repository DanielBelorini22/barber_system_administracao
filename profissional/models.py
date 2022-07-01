from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.


class Prof(models.Model):
    nome = models.CharField('Profissional', max_length=100, blank=True)
    telefone = models.CharField('Telefone', max_length=14, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissional'

    def __str__(self):
        return self.nome


class Service(models.Model):
    NOME_CHOICES = (
        ('corte', 'Corte de cabelo'),
        ('barba', 'Barba'),
        ('sobrancelha', 'Sobrancelha'),
        ('corte_sobrancelha', 'Corte de cabelo e sobrancelha'),
        ('corte_barba', 'Corte de cabelo e barba'),
        ('barba_sobrancelha', 'Barba e sobrancelha'),
        ('corte_barba_sobrancelha', 'Corte de cabelo, barba e sobrancelha'),
    )

    nome = models.CharField('Serviço', max_length=100, choices=NOME_CHOICES)
    pag = (
        ('D', 'Dinheiro'),
        ('CD', 'Cartão Débito'),
        ('CC', 'Cartão Crédito')
    )
    pagamento = models.CharField('Pagamento', max_length=2, choices=pag, blank=True)
    DURACAO_CHOICES = (
        ('meia_hora', '00:30'),
        ('uma_hora', '01:00'),
        ('uma_hora_e_meia', '01:30'),
        ('duas_horas', '02:00')
    )
    duracao = models.CharField('Duração', max_length=50, choices=DURACAO_CHOICES)
    preco = models.FloatField('Preço R$', null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome
