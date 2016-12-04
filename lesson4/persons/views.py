from django.shortcuts import render, redirect

# Create your views here.
from . import models
from . import forms
from django.http import HttpResponseRedirect


def list_persons(request):
    c = {}
    persons = models.Person.objects.all()
    c['persons'] = persons
    return render(request, template_name='persons/persons_list.html', context=c)

def person(request, person_id):
    c = {}
    person = models.Person.objects.get(id=person_id)
    c['person'] = person
    return render(request, template_name='persons/person.html', context=c)


def person_edit(request, person_id):
    c= {}
    person = models.Person.objects.get(id=person_id)
    form = forms.Person(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    c['form'] = form
    return render(request, template_name='persons/person_edit.html', context=c)


def message(request):
    form = forms.Message(request.POST or None)
    c = {}
    c['form'] = form
    if form.is_valid():
        print 'valid'
    else:
        return render(request, template_name='persons/message.html', context=c)