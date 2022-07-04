from django.forms import ModelForm, NumberInput
from cliente.models import Person
from profissional.models import Prof, Service
from agenda.models import Agenda


class ClienteForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})


class ProfForm(ModelForm):
    class Meta:
        model = Prof
        fields = '__all__'

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['preco'].widget.attrs.update({'class': 'mask-preco'})


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
        widgets = {
            'data': NumberInput(attrs={'type': 'date'}),
        }
