from django.shortcuts import render

# Create your views here.

def mainpage(request):
    x = {'name':'Maria'}
    return render(request, 'mainpage.html', x)

def ctask(request):
   return render(request, 'mainpage.html')



