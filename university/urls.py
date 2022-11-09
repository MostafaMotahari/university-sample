from django.urls import path
from .views import template

urlpatterns = [
    path('universities/', template.UniversityListView.as_view(), name='university_list'),
    path('universities/<int:pk>', template.UniversityDetailView.as_view(), name='university_detail'),
]