from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from univercity.models import University

# Create your views here.
class UniversityListView(ListView):
    model = University
    template_name = 'univercity/univercity_list.html'
    context_object_name = 'univercities'

class UniversityDetailView(DetailView):
    model = University
    template_name = 'univercity/univercity_detail.html'
    context_object_name = 'univercity'