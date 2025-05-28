from .views import index, contato, produto
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato),
    path('produto/<int:pk>', produto, name='produto')
]