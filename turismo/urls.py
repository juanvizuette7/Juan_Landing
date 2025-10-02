from django.urls import path
from . import views

app_name = 'turismo'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lugares/', views.lugares_turisticos, name='lugares'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
]