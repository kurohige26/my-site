from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vetor$', views.vetor, name='vetor'),
    url(r'^ordena_vetor$', views.ordena_vetor, name='ordena'),
]