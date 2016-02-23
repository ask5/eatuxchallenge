from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from urllib import parse
from django.core.urlresolvers import reverse, resolve
from eat.models import *
from eat.util import *
from . import *
from django.shortcuts import get_object_or_404
import csv


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
                    return redirect('application_create')
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
    """
    Create a new Application
    :param request:
    :return:
    """
    args = dict()
    if request.method == 'POST':
        form = CreateApplicatinForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.status = 1
            application.save()

            # if household participates in assistance program then redirect to the case number page
            if application.assistance_program:
                return redirect('participate')
            # if the application is being made for only a foster child goto Add Child
            elif not application.assistance_program and application.app_for_foster_child:
                return redirect('add_child')
            else:
                return redirect('children')
    else:
        form = CreateApplicatinForm(initial={ "assistance_program": None, 'app_for_foster_child': None })

    args['form'] = form
    return render(request, "eat/user/application/create.html", args)


@login_required
def application_welcome_back(request):
    """
    Welcome back screen
    :param request:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    args['percent'] = AppUtil.get_app_progress(app[0])
    result = render(request, "eat/user/application/welcome_back.html", args)
    if request.POST:
        if app[0].last_page:
            result = redirect(app[0].last_page)
        else:
            result = redirect('assistance_program')

    return result


@login_required
def assistance_program_participate(request):
    """
    if household participates in assistance program, ask for case number
    :param request:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    if request.method == 'POST':
        form = AssistanceProgramForm(request.POST, instance=app[0])
        if form.is_valid():
            _app = form.save(commit=False)
            _app.assistance_program = True
            _app.save()

            if Adult.adults.filter(application=app).exists():
                Adult.adults.filter(application=app).delete()

            if _app.app_for_foster_child:
                return redirect('add_child')
            else:
                return redirect('children')
    else:
        form = AssistanceProgramForm(instance=app[0])

    args['form'] = form
    args['nav'] = AppUtil.get_nav(nav=nav, url='participate', app=app[0])
    AppUtil.set_last_page(app[0], request.get_full_path())
    return render(request, "eat/user/application/assistance_program_participate.html", args)


@login_required
def children(request):
    """
    Displays the list of children
    :param request:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    _children = Child.children.filter(application=app[0])
    args['app'] = app[0]
    args['nav'] = AppUtil.get_nav(nav=nav, url='children', app=app[0])
    args['children'] = _children
    args['total_children'] = _children.count()
    args['earnings_pages'] = AppUtil.get_earnings_pages('children')
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    AppUtil.set_last_page(app[0], request.get_full_path())
    return render(request, "eat/user/application/child/children.html", args)


@login_required
def add_child(request):
    """
    Add a child
    :param request:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    if request.method == 'POST':
        form = AddChildForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data["first_name"]
            lname = form.cleaned_data["last_name"]
            if not Child.children.filter(first_name=fname, last_name=lname, application=app[0]).exists():
                child = form.save(commit=False)
                child.application = app[0]
                child.save()
                #if app[0].app_for_foster_child:
                #    return redirect('children')

                if app[0].assistance_program or child.foster_child or child.hmr or child.is_head_start_participant:
                    return redirect('children')
                else:
                    return redirect('child_salary', child_id=child.id)
            else:
                form.add_error('first_name', "Child with the same first and last name already exists")
    else:
        form = AddChildForm(initial={"foster_child": app[0].app_for_foster_child })
    args['form'] = form
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    args['nav'] = AppUtil.get_nav(nav=nav, url='children', app=app[0])
    return render(request, "eat/user/application/child/add_edit.html", args)


@login_required
def edit_child(request, child_id):
    """
    edit a child. NOT USED
    :param request:
    :param child_id:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    child = get_object_or_404(Child, pk=child_id, application=app[0])
    if request.method == 'POST':
        form = AddChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            if app[0].assistance_program or child.foster_child:
                return redirect('exempt_child', child_id=child.id)
            else:
                return redirect('child_salary', child_id=child.id)
    else:
        if app[0].app_for_foster_child:
            child.foster_child = True
        form = AddChildForm(instance=child)
    args['form'] = form
    args['child'] = child
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    args['nav'] = AppUtil.get_nav(nav=nav, url='children', app=app[0])
    return render(request, "eat/user/application/child/add_edit.html", args)


@login_required
def exempt_child(request, child_id):
    """
    displays a message for foster child or a child belonging to a household participating in an assistance program
    :param request:
    :param child_id:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    child = get_object_or_404(Child, pk=child_id, application=app[0])
    args['app'] = app[0]
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    args['child'] = child
    return render(request, "eat/user/application/child/exempt_child.html", args)


@login_required
def delete_child(request, child_id):
    """
    displays warning screen before deleting a child record
    :param request:
    :param child_id:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    child = get_object_or_404(Child, pk=child_id, application=app[0])
    if request.method == 'POST':
        child.delete()
        return redirect('children')
    args['child'] = child
    args['nav'] = AppUtil.get_nav(nav=nav, url='children', app=app[0])
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    return render(request, "eat/user/application/child/delete.html", args)


@login_required
def child_earnings(request, child_id):
    """
    Handles child earnings questions
    :param request:
    :param child_id:
    :return:
    """
    args = dict()
    direct = False
    app = AppUtil.get_by_user(user=request.user)
    page_name = resolve(request.path_info).url_name
    page = EarningsPage.objects.get(entity='child', name=page_name)

    if request.META.get('HTTP_REFERER'):
        if parse.urlparse(request.META.get('HTTP_REFERER')).path == reverse('children') or \
                        parse.urlparse(request.META.get('HTTP_REFERER')).path == reverse('review'):
            direct = True

    # get the current child object
    child = get_object_or_404(Child, pk=child_id, application=app[0])

    # load the FORM if the current earnings page type is 'form'
    if page.page_type == 'form':

        if request.method == 'POST':
            # process the form data after it is POSTED
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

                # redirect the user to appropriate page
                if is_direct == 'True':
                    return redirect('children')
                else:
                    if page.next.page_arg:
                        return redirect(page.next.name, child_id=child.id)
                    else:
                        return redirect(page.next.name)
        else:
            # when the form is initially loaded, fill the controls with initial values from database, if found.
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
    args['nav'] = AppUtil.get_nav(nav=nav, url='children', app=app[0])
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    AppUtil.set_last_page(child.application, request.get_full_path())
    return render(request, page.template, args)


@login_required
def adults(request):
    """
    Displays the list of adults.
    For certain household scenarios this section may not appear in the workflow or will be disabled
    especially when at least one of the following is true
         1. the household participates in an assistance program
         2. all the household children are either foster child or head start participant or homeless, migrant, runaway.
    :param request:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    _adults = Adult.adults.filter(application=app[0])
    args['app'] = app[0]
    args['adults'] = _adults
    args['nav'] = AppUtil.get_nav(nav=nav, url='adults', app=app[0])
    AppUtil.set_last_page(app[0], request.get_full_path())
    args['earnings_pages'] = AppUtil.get_earnings_pages('adults')
    args['skip'] = AppUtil.skip_household_income(app[0])
    earnings_sources = EarningSource.sources.all()

    earnings = []
    for source in earnings_sources:
        pages = EarningsPage.objects.filter(source=source, entity='adult', page_type='form')
        if pages.exists():
            earnings.append({
                'name': source,
                'pages': pages.order_by('display_order')
            })

    args['earnings'] = earnings
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    return render(request, "eat/user/application/adult/adults.html", args)


@login_required
def add_adult(request):
    """
    Add a new adult record
    :param request:
    :return:
    """
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
    args['nav'] = AppUtil.get_nav(nav=nav, url='adults', app=app[0])
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    return render(request, "eat/user/application/adult/add_edit.html", args)


@login_required
def adult_confirm(request):
    """
    confirmation screen for adults
    :param request:
    :return:
    """
    if request.method == 'POST':
        app = AppUtil.get_by_user(user=request.user)
        AppUtil.all_adults_entered(app[0])
        return redirect('contact')
    return render(request, "eat/user/application/adult/confirm.html")


@login_required
def edit_adult(request, adult_id):
    """
    Adult Edit screen. NOT USED
    :param request:
    :param adult_id:
    :return:
    """
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
    args['nav'] = AppUtil.get_nav(nav=nav, url='adults', app=app[0])
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    return render(request, "eat/user/application/adult/add_edit.html", args)


@login_required
def delete_adult(request, adult_id):
    """
    Warning screen before deleting adult record
    :param request:
    :param adult_id:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    adult = get_object_or_404(Adult, pk=adult_id, application=app[0])
    if request.method == 'POST':
        adult.delete()
        return redirect('adults')
    args['adult'] = adult
    args['nav'] = AppUtil.get_nav(nav=nav, url='adults', app=app[0])
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    return render(request, "eat/user/application/adult/delete.html", args)


@login_required
def adult_earnings(request, adult_id):
    """
    Handles adult earnings questions
    :param request:
    :param adult_id:
    :return:
    """
    args = dict()
    direct = False
    app = AppUtil.get_by_user(user=request.user)
    page_name = resolve(request.path_info).url_name
    page = EarningsPage.objects.get(entity='adult', name=page_name)

    if parse.urlparse(request.META.get('HTTP_REFERER')).path == reverse('adults') or \
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
    args['nav'] = AppUtil.get_nav(nav=nav, url='adults', app=app[0])
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    AppUtil.set_last_page(adult.application, request.get_full_path())
    return render(request, page.template, args)


@login_required
def contact(request):
    """
    Contact Form
    :param request:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    if request.method == 'POST':
        app[0].contact_form_complete = False
        app[0].save()

        # skip social security number if the household receives assistance or the application is being made for
        # foster child
        if app[0].assistance_program or app[0].app_for_foster_child:
            form = ContactFormWithOutSSN(request.POST, instance=app[0])
        else:
            form = ContactForm(request.POST, instance=app[0])

        if form.is_valid():
            _app = form.save(commit=False)
            _app.contact_form_complete = True
            _app.save()
            return redirect('race')
    else:
        if app[0].assistance_program or app[0].app_for_foster_child:
            form = ContactFormWithOutSSN(instance=app[0])
        else:
            form = ContactForm(instance=app[0])
    args['form'] = form
    args['app'] = app[0]
    args['nav'] = AppUtil.get_nav(nav=nav, url='contact', app=app[0])
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    AppUtil.set_last_page(app[0], request.get_full_path())
    return render(request, "eat/user/application/contact.html", args)


@login_required
def race(request):
    """
    Race and Ethnicity form
    :param request:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    if request.method == 'POST':
        form = RaceForm(request.POST, instance=app[0])
        if form.is_valid():
            form.save()
            return redirect('review')
    else:
        form = RaceForm(instance=app[0])

    args['form'] = form
    args['nav'] = AppUtil.get_nav(nav=nav, url='race', app=app[0])
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    AppUtil.set_last_page(app[0], request.get_full_path())
    return render(request, "eat/user/application/race.html", args)


@login_required
def review(request):
    """
    Application review page
    :param request:
    :return:
    """
    args = dict()
    app = AppUtil.get_by_user(user=request.user)
    _children = Child.children.filter(application=app[0])
    _adults = Adult.adults.filter(application=app[0])
    adult_skip = AppUtil.skip_household_income(app[0])
    total_adults_earnings = 0
    for adult in _adults:
        total_adults_earnings += adult.get_total_earning()

    # Identify the issues in the application
    issues = []
    args['app'] = app[0]

    if not _children.exists():
        issues.append("Household children information could not be found.")
    elif not app[0].app_for_foster_child and _children.count() < app[0].total_children:
        issues.append("Number of children found is less than the "
                      "total number of children mentioned during the creation of the application.")

    if not adult_skip and not _adults.exists():
        issues.append("Household Adults information could not be found.")
    elif not adult_skip and _adults.count() < app[0].total_adults:
        issues.append("Number of adults found is less than the "
                      "total number of adults mentioned during the creation of the application.")

    if not adult_skip and total_adults_earnings <= 0:
        issues.append("Total household adults' earnings can't be zero.")

    if not app[0].contact_form_complete:
        issues.append("Contact form is not complete")

    args['children'] = _children
    args['adults'] = _adults
    args['adult_skip'] = adult_skip
    args['issues'] = issues
    args['nav'] = AppUtil.get_nav(nav=nav, url='review', app=app[0])
    args['progress'] = AppUtil.get_app_progress(app=app[0])
    args['child_earnings_pages'] = AppUtil.get_earnings_pages('children')
    earnings_sources = EarningSource.sources.all()

    earnings = []
    for source in earnings_sources:
        pages = EarningsPage.objects.filter(source=source, entity='adult', page_type='form')
        if pages.exists():
            earnings.append({
                'name': source,
                'pages': pages.order_by('display_order')
            })

    args['adult_earnings_pages'] = earnings

    return render(request, "eat/user/application/review.html", args)


@login_required
def start_over(request):
    """
    confirmation page before starting over the application.
    deletes all the current application data on post
    :param request:
    :return:
    """
    if request.method == 'POST':
        app = AppUtil.get_by_user(user=request.user)
        Child.children.filter(application=app).delete()
        Adult.adults.filter(application=app).delete()
        app.delete()
        return redirect('application_create')
    return render(request, "eat/user/application/start_over.html")


@staff_member_required
def admin_dashboard(request):
    """
    Admin dashboard screen
    :param request:
    :return:
    """
    args = dict()
    args['total_users'] = User.objects.all().count()

    total_applications = Application.applications.all().count()
    apps_assistance_program = Application.applications.filter(assistance_program=True).count()
    apps_foster_child = Application.applications.filter(app_for_foster_child=True).count()
    other_applications = total_applications - (apps_assistance_program + apps_foster_child)

    args['applications'] = Application.applications.all()
    args['total_applications'] = total_applications
    args['apps_assistance_program'] = apps_assistance_program
    args['apps_foster_child'] = apps_foster_child
    args['other_applications'] = other_applications

    args['total_children'] = Child.children.all().count()
    args['students'] = Child.children.filter(is_student=True).count()
    args['non_students'] = Child.children.filter(is_student=False).count()
    args['foster_children'] = Child.children.filter(foster_child=True).count()
    args['hmr_children'] = Child.children.filter(hmr=True).count()
    args['head_start_children'] = Child.children.filter(is_head_start_participant=True).count()
    return render(request, "eat/admin/dashboard.html", args)


@staff_member_required
def admin_applications(request):
    args = dict()
    args['applications'] = Application.applications.all()
    args['title'] = 'All Applications'
    return render(request, "eat/admin/applications.html", args)


@staff_member_required
def admin_applications_foster_child(request):
    args = dict()
    args['applications'] = Application.applications.filter(app_for_foster_child=True)
    args['title'] = 'Applications for Foster Child'
    return render(request, "eat/admin/applications.html", args)


@staff_member_required
def admin_applications_assistance_program(request):
    args = dict()
    args['applications'] = Application.applications.filter(assistance_program=True)
    args['title'] = 'Applications with Assistance Program'
    return render(request, "eat/admin/applications.html", args)


@staff_member_required
def admin_application_view(request, application_id):
    args = dict()
    app = AppUtil.get(application_id)
    _children = Child.children.filter(application=app)
    _adults = Adult.adults.filter(application=app)
    total_adults_earnings = 0
    for adult in _adults:
        total_adults_earnings += adult.get_total_earning()

    args['app'] = app
    args['children'] = _children
    args['percent'] = AppUtil.get_app_progress(app)
    args['adult_skip'] = AppUtil.skip_household_income(app)
    args['adults'] = _adults
    args['child_earnings_pages'] = AppUtil.get_earnings_pages('children')
    earnings_sources = EarningSource.sources.all()

    earnings = []
    for source in earnings_sources:
        pages = EarningsPage.objects.filter(source=source, entity='adult', page_type='form')
        if pages.exists():
            earnings.append({
                'name': source,
                'pages': pages.order_by('display_order')
            })

    args['adult_earnings_pages'] = earnings
    return render(request, "eat/admin/application.html", args)


@staff_member_required
def admin_users(request):
    args = dict()
    args['users'] = User.objects.filter(is_superuser=0)
    return render(request, "eat/admin/users.html", args)


@staff_member_required
def admin_applications_export(request):
    """
    Application CSV export
    :param request:
    :return:
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="application_{}.csv"'.format(datetime.datetime.now())
    fields = ["id", "status", "enabled", "create_date", "modified_date", "total_children", "total_adults",
              "assistance_program", "app_for_foster_child", "ssn_four_digit", "no_ssn", "case_number", "first_name",
              "last_name", "middle_name", "signature", "todays_date", "street_address", "apt", "city", "state", "zip",
              "phone", "email", "ethnicity", "is_american_indian", "is_asian", "is_black", "is_hawaiian", "is_white",
              "active", "contact_form_complete", "all_adults_entered", "all_children_entered"]
    writer = csv.writer(response)
    writer.writerow(fields)
    for app in Application.applications.all():
        row = []
        for field in fields:
             row.append("" if getattr(app, field) is None else str(getattr(app, field)))
        writer.writerow(row)
    return response


@staff_member_required
def admin_children_export(request):
    """
    Children data CSV export
    :param request:
    :return:
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="children_{}.csv"'.format(datetime.datetime.now())
    fields = ["id", "application_id", "first_name", "last_name", "middle_name", "is_student", "is_head_start_participant",
              "foster_child", "hmr", "salary", "salary_frequency", "ssi_disability", "ssi_disability_frequency",
              "ssi_parent_disability", "ssi_parent_disability_frequency", "spending_money_income",
              "spending_money_income_frequency", "other_friend_income", "other_friend_income_frequency",
              "pension_income", "pension_income_frequency", "annuity_income", "annuity_income_frequency",
              "trust_income", "trust_income_frequency", "other_income", "other_income_frequency"]

    writer = csv.writer(response)
    writer.writerow(fields)
    for child in Child.children.all():
        row = []
        for field in fields:
             row.append("" if getattr(child, field) is None else str(getattr(child, field)))
        writer.writerow(row)
    return response


@staff_member_required
def admin_adults_export(request):
    """
    Adult data CSV export
    :param request:
    :return:
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="adults_{}.csv"'.format(datetime.datetime.now())
    fields = ["id", "application_id", "first_name", "middle_name", "last_name", "salary", "salary_frequency", "wages",
              "wages_frequency", "cash_bonuses", "cash_bonuses_frequency", "self_employment_income",
              "self_employment_income_frequency", "strike_benefits", "strike_benefits_frequency",
              "unemployment_insurance", "unemployment_insurance_frequency", "other_earned_income",
              "other_earned_income_frequency", "military_basic_pay", "military_basic_pay_frequency", "military_bonus",
              "military_bonus_frequency", "military_allowance", "military_allowance_frequency", "military_food",
              "military_food_frequency", "military_clothing", "military_clothing_frequency", "general_assistance",
              "general_assistance_frequency", "cash_assistance", "cash_assistance_frequency", "alimony",
              "alimony_frequency", "child_support", "child_support_frequency", "social_security_income",
              "social_security_income_frequency", "railroad_income", "railroad_income_frequency", "pension_income",
              "pension_income_frequency", "annuity_income", "annuity_income_frequency", "survivors_benefits",
              "survivors_benefits_frequency", "ssi_disability_benefits", "ssi_disability_benefits_frequency",
              "private_disability_benefits", "private_disability_benefits_frequency", "black_lung_benefits",
              "black_lung_benefits_frequency", "workers_compensation", "workers_compensation_frequency",
              "veterans_benefits", "veterans_benefits_frequency", "other_retirement_sources",
              "other_retirement_sources_frequency", "interest_income", "interest_income_frequency", "investment_income",
              "investment_income_frequency", "dividends", "dividends_frequency", "trust_or_estates_income",
              "trust_or_estates_income_frequency", "rental_income", "rental_income_frequency", "royalties_income",
              "royalties_income_frequency", "prize_winnings", "prize_winnings_frequency", "savings_withdrawn",
              "savings_withdrawn_frequency", "cash_gifts", "cash_gifts_frequency"]

    writer = csv.writer(response)
    writer.writerow(fields)
    for adult in Adult.adults.all():
        row = []
        for field in fields:
             row.append("" if getattr(adult, field) is None else str(getattr(adult, field)))
        writer.writerow(row)
    return response