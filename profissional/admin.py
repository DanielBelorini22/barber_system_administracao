from django.contrib import admin
from .models import Prof, Service


# Register your models here.

@admin.register(Prof)
class ProfAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')
    search_fields = ('nome', 'telefone')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pagamento')
    search_fields = ('nome',)
