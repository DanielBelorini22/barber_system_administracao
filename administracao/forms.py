from django.forms import ModelForm
from cliente.models import Person
from profissional.models import Prof, Service
from agenda.models import Agenda


class ClienteForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class ProfForm(ModelForm):
    class Meta:
        model = Prof
        fields = '__all__'


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
