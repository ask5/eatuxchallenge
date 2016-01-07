from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from eat.forms import RegistrationForm
from django.http import HttpResponseRedirect
from eat.models import Application
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "eat/index.html")

def non_discrimination(request):
    return render(request, "eat/non_discrimination.html")

def use_of_information(request):
    return render(request, "eat/use_of_information.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('application_home')
    else:
        form = RegistrationForm()
    result = dict()
    result['form'] = form
    return render(request, "eat/register.html", result)

def logout_view(request):
    logout(request)
    result = redirect('index')
    return result

def login_view(request):
    msg = dict()
    result = render(request, "eat/login.html")
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next_page:
                    result = redirect(next_page)
                else:
                    result = redirect('application_home')
            else:
                msg['error'] = "Account is disabled."
                result = render(request, "eat/login.html", msg)
        else:
            msg['error'] = "Incorrect Username or Password"
            result = render(request, "eat/login.html", msg)
    return result

@login_required
def application_home(request):
    app = Application.objects.filter(user = request.user.id)
    count = app.count()
    if count > 0:
        args = dict()
        args['app'] = app[0]
        result = render(request, "eat/application/home.html", args)
    else:
        result = redirect('application_start')

    return result

@login_required
def application_start(request):
    result = render(request, "eat/application/start.html")
    if request.POST:
        app = Application(
                user = request.user,
                status=1,
                create_date= datetime.now()
        )
        app.save()
        result = redirect('application_home')
    return result

