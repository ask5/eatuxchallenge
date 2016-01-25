from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from eat.forms import RegistrationForm, AssistanceProgramForm, AddChildForm, ChildSalaryForm, \
    ChildSocialSecurityForm
from django.http import HttpResponseRedirect
from eat.models import Application, Child, Adult
from eat.util import AppUtil
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
    if request.GET.get('next') is not None:
        msg['next'] = request.GET.get('next')
    result = render(request, "eat/login.html", msg)
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
                    app = AppUtil.get_by_user(user=request.user)
                    if app.count() > 0:
                        args = dict()
                        args['app'] = app[0]
                        result = redirect('application_welcome_back')
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
        result = redirect('assistance_program')
    return result


@login_required
def application_welcome_back(request):
    result = render(request, "eat/application/welcome_back.html")
    if request.POST:
        app = AppUtil.get_by_user(user=request.user)
        if app[0].last_page:
            result = redirect(app[0].last_page)
        else:
            result = redirect('assistance_program')

    return result


@login_required
def assistance_program(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    if request.method == 'POST':
        form = AssistanceProgramForm(request.POST, instance=app[0])
        if form.is_valid():
            form.save()
            return redirect('confirm_assistance_program')
    else:
        form = AssistanceProgramForm(instance=app[0])
    args['form'] = form
    AppUtil.set_last_page(app[0], request.path_info)
    return render(request, "eat/application/assistance_program.html", args)


@login_required
def confirm_assistance_program(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    args['app'] = app[0]
    return render(request, "eat/application/confirm_assistance_program.html", args)

@login_required
def children(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    c = Child.children.filter(application=app[0])
    args['app'] = app[0]
    args['children'] = c
    AppUtil.set_last_page(app[0], request.path_info)
    return render(request, "eat/application/child/children.html", args)


@login_required
def add_child(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    if request.method == 'POST':
        form = AddChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.application = app[0]
            child.save()
            if app[0].assistance_program:
                return redirect('children')
            else:
                return redirect('child_salary', child_id=child.id)
    else:
        form = AddChildForm()
    args['form'] = form
    return render(request, "eat/application/child/add.html", args)


@login_required
def child_salary(request, child_id):
    args = dict()
    child = Child.children.get(pk=child_id)
    if request.method == 'POST':
        form = ChildSalaryForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect('child_social_security_income', child_id=child.id)
    else:
        form = ChildSalaryForm(instance=child)
    args['form'] = form
    args['child'] = child
    return render(request, "eat/application/child/salary.html", args)


@login_required
def child_social_security_income(request, child_id):
    args = dict()
    child = Child.children.get(pk=child_id)
    if request.method == 'POST':
        form = ChildSocialSecurityForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
    else:
        form = ChildSocialSecurityForm(instance=child)
    args['form'] = form
    args['child'] = child
    return render(request, "eat/application/child/social_security_income.html", args)


@login_required
def adults(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    a = Adult.adults.filter(application=app[0])
    args['app'] = app[0]
    args['adults'] = a
    AppUtil.set_last_page(app[0], request.path_info)
    return render(request, "eat/application/adult/adults.html", args)

@login_required
def add_adult(request):
    app = AppUtil.get_by_user(user=request.user)
    return render(request, "eat/application/adult/add.html")

@login_required
def contact(request):
    app = AppUtil.get_by_user(user=request.user)
    AppUtil.set_last_page(app[0], request.path_info)
    return render(request,"eat/application/contact.html")