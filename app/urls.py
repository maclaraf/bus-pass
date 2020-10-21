from django.urls import path
from . import views

urlpatterns = [
    path('', views.pass_cad, name='pass_cad'),
]