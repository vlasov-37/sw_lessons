from .models import Student, RecordBook
from django.views import generic


class MainView(generic.ListView):
    template_name = 'core/main.html'
    context_object_name = 'all_students'

    def get_queryset(self):
        return Student.objects.order_by('surname')


class DetailView(generic.DetailView):
    model = RecordBook
    template_name = 'core/detail.html'


class Check(generic.ListView):
    model = RecordBook
    template_name = 'core/index.html'
