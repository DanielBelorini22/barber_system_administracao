from django.db import models
from cliente.models import Person
from profissional.models import Prof, Service


# Create your models here.

class Agenda(models.Model):
    cliente = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    profissional = models.ForeignKey(Prof, on_delete=models.CASCADE, null=True, blank=True)
    servico = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    STATUS_CHOICES = (
        ('A', 'Agendado'),
        ('F', 'Finalizado'),
        ('C', 'Cancelado')
    )

    status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES, null=True, blank=True)
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2, null=True, blank=True)

    pag = (
        ('D', 'Dinheiro'),
        ('CD', 'Cartão Débito'),
        ('CC', 'Cartão Crédito')
    )

    pagamento = models.CharField('Pagamento', max_length=2, choices=pag, null=True, blank=True)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agenda'

    def __str__(self):
        return self.cliente
