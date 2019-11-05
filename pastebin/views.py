from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import paste
from django.http import HttpRequest,HttpResponse
# Create your views here.

class Create (CreateView):
    model = paste
    fields = ['text','name']

def viewAll (random):
    return HttpResponse('This is a valid view')

