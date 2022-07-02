from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.cliente, name='cliente'),
    path('clientes/', views.clientes, name='clientes'),
    path('prof/', views.prof, name='prof'),
    path('profissionais/', views.profissionais, name='profissionais'),
    path('service/', views.service, name='service'),
    path('services/', views.services, name='services'),
    path('agenda/', views.agenda, name='agenda'),
    path('lista/', views.lista, name='lista'),
    path('editar/<int:id_agenda>/', views.editar, name='editar'),
    path('deletar/<int:id_agenda>/', views.deletar, name='deletar'),
    path('edita_cliente/<int:id_cliente>/', views.edita_cliente, name='edita_cliente'),
    path('deleta_cliente/<int:id_cliente>/', views.deleta_cliente, name='deleta_cliente'),
    path('edita_profissional/<int:id_profissional>/', views.edita_profissional, name='edita_profissional'),
    path('deleta_profissional/<int:id_profissional>/', views.deleta_profissional, name='deleta_profissional'),
    path('edita_servico/<int:id_servico>/', views.edita_servico, name='edita_servico'),
    path('deleta_servico/<int:id_servico>/', views.deleta_servico, name='deleta_servico'),
    path('relatorio_cliente/', views.relatorio_cliente, name='relatorio_cliente'),
    path('relatorio_profissional/', views.relatorio_profissional, name='relatorio_profissional'),
    path('relatorio_servico/', views.relatorio_servico, name='relatorio_servico'),
]
