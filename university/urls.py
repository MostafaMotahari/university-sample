from django.urls import path
from .views import template

urlpatterns = [
    path('university/list', template.UniversityListView.as_view(), name='university_list'),
    path('university/details/<int:pk>', template.UniversityDetailView.as_view(), name='university_detail'),
]