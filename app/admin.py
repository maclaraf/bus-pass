from django.contrib import admin

from .models import Cadastro
from .models import Recarga
from .models import Utilizacao

admin.site.register(Cadastro)
admin.site.register(Recarga)
admin.site.register(Utilizacao)
