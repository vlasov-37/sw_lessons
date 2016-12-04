#coding: utf-8
from django.shortcuts import render
from polls import models
# Create your views here.
def index(request):
    blogentry_mod = models.BlogEntry.objects.all()[0]
    context = {'blogentry_mod':blogentry_mod}
    return render(request, 'index.html', context) # возвращаем функцию рендер(отрисовать) с аргументами реквест
    # имя шаблона и контекст таким образом при обращении к данной функции она отрисует заданный шаблон с заданным контекстом
