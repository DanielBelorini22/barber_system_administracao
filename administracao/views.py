from django.shortcuts import render, redirect, get_object_or_404
from cliente.models import Person
from profissional.models import Prof, Service
from .forms import ClienteForm, ProfForm, ServiceForm, AgendaForm
from agenda.models import Agenda
from datetime import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
    data = datetime.now()
    lista = Person.objects.all()
    paginator = Paginator(lista, 3)
    page = request.GET.get('page')
    lista = paginator.get_page(page)
    return render(request, 'index.html', {'lista': lista, 'data': data})


@login_required
def cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'administracao/clienteform.html', {'form': form})


@login_required
def prof(request):
    if request.method == 'POST':
        form = ProfForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfForm()
    return render(request, 'administracao/profform.html', {'form': form})


@login_required
def service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ServiceForm()
    return render(request, 'administracao/serviceform.html', {'form': form})


@login_required
def agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = AgendaForm()
    return render(request, 'administracao/agendaform.html', {'form': form})


@login_required
def lista(request):
    relation = Agenda.objects.all()
    paginator = Paginator(relation, 3)
    page = request.GET.get('page')
    relation = paginator.get_page(page)
    return render(request, 'administracao/lista.html', {'relation': relation})


@login_required
def editar(request, id_agenda):
    edite = get_object_or_404(Agenda, id=id_agenda)
    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=edite)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = AgendaForm(instance=edite)
    return render(request, 'administracao/agendaform.html', {'form': form})


@login_required
def deletar(request, id_agenda):
    exclui = Agenda.objects.get(id=id_agenda).delete()
    return redirect('lista')


@login_required
def edita_cliente(request, id_cliente):
    ed = get_object_or_404(Person, id=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=ed)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm(instance=ed)
    return render(request, 'administracao/clienteform.html', {'form': form})


@login_required
def deleta_cliente(request, id_cliente):
    exclui_cliente = Person.objects.get(id=id_cliente).delete()
    return redirect('home')
