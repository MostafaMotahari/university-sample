from django.urls import path
from .views import template

urlpatterns = [
    path('univercities/', template, name='template'),
]