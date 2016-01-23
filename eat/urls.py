from django.conf.urls import url
from django.views.generic import TemplateView
from eat import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="eat/index.html"), name='index'),
    url(r'^non_discrimination', TemplateView.as_view(template_name="eat/non_discrimination.html"),
        name="non_discrimination"),
    url(r'^use-of-information', TemplateView.as_view(template_name="eat/use_of_information.html"),
        name="use_of_information"),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login_view, name="login"),
    url(r'^logout', views.logout_view, name="logout"),
    url(r'^app/welcome', views.application_welcome_back, name='application_welcome_back'),
    url(r'^app/create', views.application_create, name='application_create'),
    url(r'^app/step2', views.step_2, name='step-2'),
    url(r'^app/children', views.children, name='children'),
    url(r'^app/add_child', views.add_child, name='add_child'),
    url(r'^app/adults', views.adults, name='adults'),
    url(r'^app/add_adult', views.add_adult, name='add_adult'),
    url(r'^app/contact', views.contact, name='contact'),
]