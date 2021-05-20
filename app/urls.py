from django.urls import path
from . import views

urlpatterns = [
    path('', views.pass_index, name='pass_index'),
    path('cadastrar/', views.pass_cad, name='pass_cad'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
]