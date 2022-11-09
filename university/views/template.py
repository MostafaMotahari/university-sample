from django.views.generic.detail import DetailView
from django_filters.views import FilterView
from university.models import University
from university.filters import UniversityFilter

# Create your views here.
class UniversityListView(FilterView):
    model = University
    context_object_name = 'universities'
    template_name = 'university_list.html'
    paginate_by = 10
    filterset_class = UniversityFilter


class UniversityDetailView(DetailView):
    model = University
    template_name = 'university_detail.html'
    context_object_name = 'university'
