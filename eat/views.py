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
    template = "eat/application/start.html"
    result = dict()
    app = Application.objects.filter(user = request.user.id)
    count = app.count()
    if count > 0:
        template = "eat/application/home.html"
        app = app[0]
    elif count <= 0 and request.POST:
        app = Application(
                user = request.user,
                status=1,
                create_date= datetime.now()
        )
        app.save()
        template = "eat/application/home.html"
    else:
        template = "eat/application/start.html"

    result['app'] = app
    return render(request, template, result)
