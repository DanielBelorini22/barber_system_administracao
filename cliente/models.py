from django.db import models


# Create your models here.


class Person(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=True)
    cpf = models.CharField('CPF', max_length=14, blank=True)
    telefone = models.CharField('Telefone', max_length=9, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome
