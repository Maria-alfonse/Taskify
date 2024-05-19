
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import User
def home_view(request):
    return render(request, 'home.html')

def login(request):
    msg = None
    if request.method == 'POST':
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.filter(email=email).first()
        if user :
            if user.password==password:
                if user.is_admin:
                    return redirect('admin_home')
                else:
                    return redirect('teacher_home')
    else:
        form = SignUpForm()
        return render(request, 'login.html', {'form': form, 'msg': msg})

def signup(request):
    form = SignUpForm(request.POST.get('username'))
    msg = None
    if request.method == 'POST':
        username=request.POST['username']
        password1=request.POST['password']
        password2=request.POST['confirmpassword']
        email=request.POST['email']
        choose=request.POST['choose']
        if choose=='admin':
            is_admin=True
        else:
            is_admin=False 
        user = User(username=username, password=password1,email=email,is_admin=is_admin)
        #user = authenticate(username=username, password=password1,confirmpassword=password2,email=email,choose=choose)
        user.save()
        #return user
        if user is not None:
            if user.is_admin:
                #login(request)
                return redirect('admin_home')
            elif not user.is_admin:
                #login(request)
                return redirect('teacher_home')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Invalid credentials'
    else:
        msg = 'Error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg}) 

@login_required
def admin_home(request):
    return render(request, 'admin_home.html')

@login_required
def teacher_home(request):
    return render(request, 'teacher_home.html')
  




