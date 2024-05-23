from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import User

<<<<<<< HEAD
=======
def home_view(request):
    return render(request, 'home.html')
>>>>>>> d5ae8f8d412cb020e54d33e70f3fc863a2f8569c

def auth(request):
    if request.method == 'POST':
        if request.POST.get('username'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            choose = request.POST.get('choose')
            is_admin = choose == 'admin'
            user = User(username=username, password=password, email=email, is_admin=is_admin)
            user.save()
            if user:
                if user.is_admin:
<<<<<<< HEAD
                    return redirect('showTask')
                else:
                    return redirect('teacherhome')
=======
                    return redirect('admin_home')
                else:
                    return redirect('teacherhome', {'name': username})
>>>>>>> d5ae8f8d412cb020e54d33e70f3fc863a2f8569c
            else:
                return HttpResponse('Invalid credentials')
        else:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.filter(email=email).first()
            if user:
                if user.password == password:
                    if user.is_admin:
                        return redirect('showTask')
                    else:
                        return redirect('teacherhome', {'name': user.username})
                else:
                    return HttpResponse('Invalid credentials')
            else:
                return HttpResponse('Invalid credentials')
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()
        if user:
            if user.password == password:
                if user.is_admin:
                    return redirect('showTask')
                else:
                    return redirect('teacherhome', {'name': user.username})
            else:
                return HttpResponse('Invalid credentials')
    return render(request, 'login.html')

def signup(request):
    form = SignUpForm(request.POST.get('username'))
    msg = None
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['confirmpassword']
        email = request.POST['email']
        choose = request.POST['choose']
        is_admin = choose == 'admin'
        user = User(username=username, password=password1, email=email, is_admin=is_admin)
        user.save()
        if user:
            if user.is_admin:
<<<<<<< HEAD
                return redirect('showTask')
            else:
                return redirect('teacherhome')
=======
                return redirect('admin_home')
            else:
                return redirect('teacherhome', {'name': username})
>>>>>>> d5ae8f8d412cb020e54d33e70f3fc863a2f8569c
        else:
            msg = 'Invalid credentials'
    else:
        msg = 'Error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

<<<<<<< HEAD
=======
def admin_home(request):
    return render(request, '../templates/AdminHome/AdminHome.html')
>>>>>>> d5ae8f8d412cb020e54d33e70f3fc863a2f8569c

def teacher_home(request, name):
    context = {'name': name}
    return render(request, 'availableTasks/availableTasks.html', context)
<<<<<<< HEAD

def home_view(request):
    return render(request,'home.html')
=======
>>>>>>> d5ae8f8d412cb020e54d33e70f3fc863a2f8569c
