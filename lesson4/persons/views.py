from django.shortcuts import render

# Create your views here.
from . import models


def list_persons(request):
    c = {}
    persons = models.Person.objects.all()
    c['persons'] = persons
    return render(request, template_name='persons/persons_list.html', context=c)