from django.urls import path
from django_filters.views import FilterView
from university.filters import UniversityFilter
from .views import template

urlpatterns = [
    path('university/list', template.UniversityListView.as_view(), name='university_list'),
    path('university/details/<int:pk>', template.UniversityDetailView.as_view(), name='university_detail'),
]