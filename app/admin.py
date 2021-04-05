from django.contrib import admin

from .models import Cadastro
from .models import Recarga
from .models import Utilizacao

admin.site.register(Cadastro)


# admin.site.register(Utilizacao)
@admin.register(Utilizacao)
class UtilizacaoAdmin(admin.ModelAdmin):
    list_display = (
        'alters_data',
        'usuario',
        'valor',
    )


# admin.site.register(Recarga)
@admin.register(Recarga)
class RecargaAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'saldo_atual',
    )
