from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from datetime import datetime
from os.path import split
from urllib import parse
from django.core.urlresolvers import reverse, resolve
from eat.models import *
from eat.forms import *
from eat.util import *
from . import *
import operator
from django.shortcuts import get_object_or_404

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
    result = render(request, "eat/user/application/create.html")
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
    result = render(request, "eat/user/application/welcome_back.html")
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
    AppUtil.set_last_page(app[0], request.get_full_path())
    return render(request, "eat/user/application/assistance_program.html", args)


@login_required
def confirm_assistance_program(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    args['app'] = app[0]
    return render(request, "eat/user/application/confirm_assistance_program.html", args)


@login_required
def children(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    c = Child.children.filter(application=app[0])
    args['app'] = app[0]
    args['children'] = c

    earnings_categories = list()
    for k, v in child_earnings_meta_data.items():
        if v['type'] == 'earnings':
            earnings_categories.append(v)

    args['earnings_categories'] = sorted(earnings_categories, key=lambda category: (category['order']))
    AppUtil.set_last_page(app[0], request.get_full_path())
    return render(request, "eat/user/application/child/children.html", args)


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
    return render(request, "eat/user/application/child/add_edit.html", args)


@login_required
def edit_child(request, child_id):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    child = get_object_or_404(Child, pk=child_id, application=app[0])
    if request.method == 'POST':
        form = AddChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect('children')
    else:
        form = AddChildForm(instance=child)
    args['form'] = form
    return render(request, "eat/user/application/child/add_edit.html", args)


@login_required
def delete_child(request, child_id):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    child = get_object_or_404(Child, pk=child_id, application=app[0])
    if request.method == 'POST':
        child.delete()
        return redirect('children')
    args['child'] = child
    return render(request, "eat/user/application/child/delete.html", args)


@login_required
def child_earnings(request, child_id):
    args = dict()
    direct = False
    app = AppUtil.get_by_user(user=request.user)
    url = resolve(request.path_info).url_name
    meta = child_earnings_meta_data[url]
    if request.META.get('HTTP_REFERER'):
        if parse.urlparse(request.META.get('HTTP_REFERER')).path == reverse('children'):
            direct = True

    child = get_object_or_404(Child, pk=child_id, application=app[0])

    if meta['type'] == 'earnings':
        if request.method == 'POST':
            form = EarningsForm(request.POST)
            if form.is_valid():
                earning = form.cleaned_data['earning']
                frequency = form.cleaned_data['frequency']
                is_direct = request.POST.get('is_direct')
                if earning == "" or earning is None or earning == 0:
                    earning = 0
                    frequency = None
                setattr(child, meta['value_field'], earning)
                setattr(child, meta['frequency_field'], frequency)

                child.save()
                if is_direct == 'True':
                    return redirect('children')
                else:
                    next_page = meta['next_page']
                    if next_page['has_child_id']:
                        return redirect(next_page['name'], child_id=child.id)
                    else:
                        return redirect(next_page['name'])
        else:
            data = {
                'earning': getattr(child, meta['value_field']),
                'frequency': getattr(child, meta['frequency_field'])
            }
            form = EarningsForm(initial=data)
        args['form'] = form

    args['direct'] = direct
    args['child_id'] = child.id
    args['previous_page'] = meta['previous_page']
    args['heading'] = meta['headline'].format(child.first_name)
    args['tip'] = meta['help_tip']
    AppUtil.set_last_page(child.application, request.get_full_path())
    return render(request, meta['template'], args)


@login_required
def adults(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    a = Adult.adults.filter(application=app[0])
    args['app'] = app[0]
    args['adults'] = a
    earnings_categories = list()
    for k, v in adult_earnings_meta_data.items():
        if v['type'] == 'earnings':
            earnings_categories.append(v)

    args['earnings_categories'] = sorted(earnings_categories, key=lambda category: (category['order']))

    AppUtil.set_last_page(app[0], request.get_full_path())
    return render(request, "eat/user/application/adult/adults.html", args)


@login_required
def add_adult(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    if request.method == 'POST':
        form = AddAdultForm(request.POST)
        if form.is_valid():
            adult = form.save(commit=False)
            adult.application = app[0]
            adult.save()
            return redirect('adult_salary', adult_id=adult.id)
    else:
        form = AddAdultForm()
    args['form'] = form
    return render(request, "eat/user/application/adult/add_edit.html", args)


@login_required
def edit_adult(request, adult_id):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    adult = get_object_or_404(Adult, pk=adult_id, application=app[0])

    if request.method == 'POST':
        form = AddAdultForm(request.POST, instance=adult)
        if form.is_valid():
            form.save()
            return redirect('adults')
    else:
        form = AddAdultForm(instance=adult)
    args['form'] = form
    return render(request, "eat/user/application/adult/add_edit.html", args)


@login_required
def delete_adult(request, adult_id):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    adult = get_object_or_404(Adult, pk=adult_id, application=app[0])
    if request.method == 'POST':
        adult.delete()
        return redirect('adults')
    args['adult'] = adult
    return render(request, "eat/user/application/adult/delete.html", args)


@login_required
def adult_earnings(request, adult_id):
    args = dict()
    direct = False
    url = resolve(request.path_info).url_name
    meta = adult_earnings_meta_data[url]
    if request.META.get('HTTP_REFERER'):
        if parse.urlparse(request.META.get('HTTP_REFERER')).path == reverse('adults'):
            direct = True
    app = AppUtil.get_by_user(user=request.user)
    adult = get_object_or_404(Adult, pk=adult_id, application=app[0])

    if meta['type'] == 'earnings':
        if request.method == 'POST':
            form = EarningsForm(request.POST)
            if form.is_valid():
                earning = form.cleaned_data['earning']
                frequency = form.cleaned_data['frequency']
                if earning == "" or earning is None or earning == 0:
                    earning = 0
                    frequency = None
                setattr(adult, meta['value_field'], earning)
                setattr(adult, meta['frequency_field'], frequency)
                adult.save()

                is_direct = request.POST.get('is_direct')
                if is_direct == 'True':
                    return redirect('adults')
                else:
                    next_page = meta['next_page']
                    if next_page['has_adult_id']:
                        return redirect(next_page['name'], adult_id=adult.id)
                    else:
                        return redirect(next_page['name'])
        else:
            data = {
                'earning': getattr(adult, meta['value_field']),
                'frequency': getattr(adult, meta['frequency_field'])
            }
            form = EarningsForm(initial=data)
        args['form'] = form

    args['direct'] = direct
    args['adult_id'] = adult.id
    args['next_page'] = meta['next_page']
    args['previous_page'] = meta['previous_page']
    if 'skip_to_page' in meta:
        args['skip_to_page'] = meta['skip_to_page']
    args['heading'] = meta['headline'].format(adult.first_name)
    args['tip'] = meta['help_tip']
    AppUtil.set_last_page(adult.application, request.get_full_path())
    return render(request, meta['template'], args)


@login_required
def contact(request):
    app = AppUtil.get_by_user(user=request.user)
    AppUtil.set_last_page(app[0], request.get_full_path())
    return render(request, "eat/user/application/contact.html")