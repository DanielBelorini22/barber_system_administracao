from django.contrib import admin
from .models import Agenda


# Register your models here.

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servico', 'profissional', 'data')
    search_fields = ('cliente', 'servico', 'profissional')
