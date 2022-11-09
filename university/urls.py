from django.urls import path
from .views import template

urlpatterns = [
    path('universities/', template.UniversityListView.as_view(), name='template'),
]