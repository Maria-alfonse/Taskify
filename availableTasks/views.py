from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def availableTasks(request):
    template=loader.get_template('availableTasks.html')
    return HttpResponse(template.render())
