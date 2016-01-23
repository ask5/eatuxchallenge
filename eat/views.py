from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from eat.forms import RegistrationForm, Step2Form
from django.http import HttpResponseRedirect
from eat.models import Application, Child, Adult
from eat.util import App
from datetime import datetime


# Create your views here.
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
                    app = App.get_by_user(user=request.user)
                    # if application is found, redirect to the welcome page
                    if app.count() > 0:
                        request.session['app_id'] = app[0].id
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
        request.session['app_id'] = app.id
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
    args = dict()
    app = App.get(request.session.get('app_id'))
    if request.method == 'POST':
        form = Step2Form(request.POST, instance=app)
        if form.is_valid():
            app = form.save()
            app.set_status(status=2)
            return redirect('children')
    else:
        form = Step2Form(instance=app)
    args['form'] = form
    return render(request, "eat/application/step_2.html", args)


@login_required
def children(request):
    args = dict()
    app = App.get_by_user(user=request.user)
    c = Child.children.filter(application=app)
    args['app'] = app[0]
    args['children'] = c
    return render(request,"eat/application/children.html", args)


@login_required
def add_child(request):
    return render(request, "eat/application/child_add.html")


@login_required
def adults(request):
    args = dict()
    app = App.get_by_user(user=request.user)
    a = Adult.adults.filter(application=app)
    args['app'] = app[0]
    args['adults'] = a
    return render(request,"eat/application/adults.html", args)

@login_required
def add_adult(request):
    return render(request, "eat/application/adult_add.html")

@login_required
def contact(request):
    return render(request,"eat/application/contact.html")