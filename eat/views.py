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
    args['nav'] = AppUtil.get_nav(nav=nav, url='assistance_program')
    AppUtil.set_last_page(app[0], request.get_full_path())
    return render(request, "eat/user/application/assistance_program.html", args)


@login_required
def confirm_assistance_program(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    args['app'] = app[0]
    return render(request, "eat/user/application/confirm_assistance_program.html", args)


@login_required
def review(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    _children = Child.children.filter(application=app[0])
    _adults = Adult.adults.filter(application=app[0])
    args['app'] = app[0]
    args['children'] = _children
    args['adults'] = _adults
    args['nav'] = AppUtil.get_nav(nav=nav, url='review')
    args['child_earnings_pages'] = AppUtil.get_earnings_pages('children')
    args['adult_earnings_pages'] = AppUtil.get_earnings_pages('adults')
    return render(request, "eat/user/application/review.html", args)


@login_required
def children(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    _children = Child.children.filter(application=app[0])
    args['app'] = app[0]
    args['nav'] = AppUtil.get_nav(nav=nav, url='children')
    args['children'] = _children
    args['earnings_pages'] = AppUtil.get_earnings_pages('children')
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
            return redirect('child_salary', child_id=child.id)
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
    page_name = resolve(request.path_info).url_name
    page = EarningsPage.objects.get(entity='child', name=page_name)

    if request.META.get('HTTP_REFERER'):
        if parse.urlparse(request.META.get('HTTP_REFERER')).path == reverse('children') or \
                        parse.urlparse(request.META.get('HTTP_REFERER')).path == reverse('review'):
            direct = True

    child = get_object_or_404(Child, pk=child_id, application=app[0])

    if page.page_type == 'form':
        if request.method == 'POST':
            form = EarningsForm(request.POST)
            if form.is_valid():
                earning = form.cleaned_data['earning']
                frequency = form.cleaned_data['frequency']
                is_direct = request.POST.get('is_direct')
                if earning == "" or earning is None or earning == 0:
                    earning = 0
                    frequency = None
                setattr(child, page.value_field, earning)
                setattr(child, page.frequency_field, frequency)
                child.save()
                if is_direct == 'True':
                    return redirect('children')
                else:
                    if page.next.page_arg:
                        return redirect(page.next.name, child_id=child.id)
                    else:
                        return redirect(page.next.name)
        else:
            data = {
                'earning': getattr(child, page.value_field),
                'frequency': getattr(child, page.frequency_field)
            }
            form = EarningsForm(initial=data)
        args['form'] = form

    args['direct'] = direct
    args['child_id'] = child.id
    args['previous_page'] = EarningsPage.objects.get(next=page)
    args['next_page'] = page.next
    args['skip_to_page'] = page.skip_to
    args['heading'] = page.headline.format(child.first_name)
    args['tip'] = page.help_tip
    AppUtil.set_last_page(child.application, request.get_full_path())
    return render(request, page.template, args)


@login_required
def adults(request):
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    _adults = Adult.adults.filter(application=app[0])
    args['app'] = app[0]
    args['adults'] = _adults
    args['nav'] = AppUtil.get_nav(nav=nav, url='adults')
    AppUtil.set_last_page(app[0], request.get_full_path())
    args['earnings_pages'] = AppUtil.get_earnings_pages('adults')
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
            return redirect('adult_salary', adult_id=adult.id)
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
    app = AppUtil.get_by_user(user=request.user)
    page_name = resolve(request.path_info).url_name
    page = EarningsPage.objects.get(entity='adult', name=page_name)

    if parse.urlparse(request.META.get('HTTP_REFERER')).path == reverse('children') or \
                    parse.urlparse(request.META.get('HTTP_REFERER')).path == reverse('review'):
            direct = True

    adult = get_object_or_404(Adult, pk=adult_id, application=app[0])

    if page.page_type == 'form':
        if request.method == 'POST':
            form = EarningsForm(request.POST)
            if form.is_valid():
                earning = form.cleaned_data['earning']
                frequency = form.cleaned_data['frequency']
                is_direct = request.POST.get('is_direct')
                if earning == "" or earning is None or earning == 0:
                    earning = 0
                    frequency = None
                setattr(adult, page.value_field, earning)
                setattr(adult, page.frequency_field, frequency)
                adult.save()
                if is_direct == 'True':
                    return redirect('adults')
                else:
                    if page.next.page_arg:
                        return redirect(page.next.name, adult_id=adult.id)
                    else:
                        return redirect(page.next.name)
        else:
            data = {
                'earning': getattr(adult, page.value_field),
                'frequency': getattr(adult, page.frequency_field)
            }
            form = EarningsForm(initial=data)
        args['form'] = form

    args['direct'] = direct
    args['adult_id'] = adult.id
    args['previous_page'] = EarningsPage.objects.get(next=page)
    args['next_page'] = page.next
    args['skip_to_page'] = page.skip_to
    args['heading'] = page.headline.format(adult.first_name)
    args['tip'] = page.help_tip
    AppUtil.set_last_page(adult.application, request.get_full_path())
    return render(request, page.template, args)


@login_required
def contact(request):
    app = AppUtil.get_by_user(user=request.user)
    AppUtil.set_last_page(app[0], request.get_full_path())
    return render(request, "eat/user/application/contact.html")