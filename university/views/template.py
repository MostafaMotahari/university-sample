import django
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core import paginator
from university.models import University, City, Country

# Create your views here.
class UniversityListView(ListView):
    model = University
    context_object_name = 'universities'
    template_name = 'university_list.html'

    def get_context_data(self, **kwargs):
        context = super(UniversityListView, self).get_context_data(**kwargs)
        name_filter = self.request.GET.get('name', None)
        country_filter = self.request.GET.get('country', None)
        city_filter = self.request.GET.get('city', None)
        context['universities'] = University.objects.all()

        if name_filter:
            context['universities'] = context['universities'].filter(name__icontains=name_filter)

        if country_filter:
            context['universities'] = context['universities'].filter(city__country__name__icontains=country_filter)

        if city_filter:
            context['universities'] = context['universities'].filter(city__name__icontains=city_filter)

        university_paginator = paginator.Paginator(context['universities'], 2)
        page = self.request.GET.get('page')
        university_page = university_paginator.get_page(page)

        context['universities'] = university_page
        context['cities'] = City.objects.all()
        context['countries'] = Country.objects.all()
        return context


class UniversityDetailView(DetailView):
    model = University
    template_name = 'university_detail.html'
    context_object_name = 'university'
