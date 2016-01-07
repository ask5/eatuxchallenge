from django.conf.urls import url

from eat import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login_view, name="login"),
    url(r'^logout', views.logout_view, name="logout"),
    url(r'^non_discrimination', views.non_discrimination, name="non_discrimination"),
    url(r'^use-of-information', views.use_of_information, name="use_of_information"),
    url(r'^app/home', views.application_home, name='application_home'),
]