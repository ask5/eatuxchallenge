from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from eat.forms import RegistrationForm, StepForm
from django.http import HttpResponseRedirect
from eat.models import Application
from datetime import datetime


# Create your views here.
def index(request):
    """
    This the home page of the website
    :param request:
    :return:
    """
    return render(request, "eat/index.html")


def non_discrimination(request):
    return render(request, "eat/non_discrimination.html")


def use_of_information(request):
    return render(request, "eat/use_of_information.html")


def register(request):
    """
    User registration page
    :param request:
    :return:
    """
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
    """
    login view
    :param request:
    :return:
    """
    msg = dict()
    result = render(request, "eat/login.html")
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        # do authentication
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # if page url is passed in the next page parameter, redirect to it.
                if next_page:
                    result = redirect(next_page)
                else:
                    # check if the user has created an application.
                    app = Application.objects.filter(user=request.user.id)
                    # if application is found, redirect to the welcome page
                    if app.count() > 0:
                        args = dict()
                        args['app'] = app[0]
                        result = redirect('application_welcome_back')
                    # otherwise ask the user to create the application.
                    else:
                        result = redirect('application_create')
            else:
                msg['error'] = "Account is disabled."
                result = render(request, "eat/login.html", msg)
        else:
            msg['error'] = "Incorrect Username or Password"
            result = render(request, "eat/login.html", msg)
    return result


@login_required
def application_create(request):
    result = render(request, "eat/application/create.html")
    if request.POST:
        app = Application(
            user=request.user,
            status=1,
            create_date=datetime.now()
        )
        app.save()
        result = redirect('step-2')
    return result


@login_required
def application_welcome_back(request):
    """
    The welcome back screen, this is the screen from where user can jump to the place where he left off
    :param request:
    :return:
    """
    result = render(request, "eat/application/welcome_back.html")
    if request.POST:
        result = redirect('step-2')
    return result


@login_required
def step_2(request):
    if request.method == 'POST':
        form = StepForm(request.POST)
        if form.is_valid():
            assistance_program = form.cleaned_data['assistanceProgram']
            case_number = form.cleaned_data['caseNumber']
            app = Application.objects.get(user=request.user.id)
            app.assistance_program = assistance_program
            if assistance_program:
                app.case_number = case_number
            else:
                app.case_number = ''
    else:
        form = StepForm()
    result = dict()
    result['form'] = form
    return render(request, "eat/application/step_2.html", result)

@login_required
def add_child(request):
    return render(request,"eat/application/add_child.html")

@login_required
def contact(request):
    return render(request,"eat/application/contact.html")