from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Todoapp


def index(request):

   mylist = Todoapp.objects.all().values()
   template = loader.get_template('list.html')
   context = {
    'mylist': mylist,
  }
   return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))


def addrecord(request):
  x = request.POST['task']
  todoapp = Todoapp(task=x)
  todoapp.save()
  return HttpResponseRedirect(reverse('index'))


def delete(request, id):
  todoapp = Todoapp.objects.get(id=id)
  todoapp.delete()
  return HttpResponseRedirect(reverse('index'))


def update(request, id):
  todoapp = Todoapp.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'todoapp': todoapp,
  }
  return HttpResponse(template.render(context, request))


def updaterecord(request, id):
  task = request.POST['task']
  todoapp = Todoapp.objects.get(id=id)
  todoapp.task = task
  todoapp.save()
  return HttpResponseRedirect(reverse('index'))
