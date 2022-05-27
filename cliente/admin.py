from django.contrib import admin
from .models import Person


# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone')
    search_fields = ('nome', 'cpf', 'telefone')
