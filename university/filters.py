import django_filters
from django.db import models
from university.models import University

class UniversityFilter(django_filters.FilterSet):
    class Meta:
        model = University
        exclude = ('logo', )
        fields = ['name', 'city', 'city__country']