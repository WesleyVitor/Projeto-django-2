from django.contrib import admin
from .models import Funcionario, Cargo, Servico, Recurso
# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cargo','ativo','modificado','bio')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo','ativo','modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','icone','ativo')

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome','icone','descricao')