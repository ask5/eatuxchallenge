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
    url(r'^app/assistance_program/$', views.assistance_program, name='assistance_program'),
    url(r'^app/assistance_program/confirm', views.confirm_assistance_program, name='confirm_assistance_program'),
    url(r'^app/children/$', views.children, name='children'),
    url(r'^app/children/add/$', views.add_child, name='add_child'),
    url(r'^app/children/(?P<child_id>[0-9]+)/edit', views.edit_child, name='edit_child'),
    url(r'^app/children/(?P<child_id>[0-9]+)/delete', views.delete_child, name='delete_child'),
    url(r'^app/children/(?P<child_id>[0-9]+)/salary', views.child_earnings, name='child_salary'),
    url(r'^app/children/(?P<child_id>[0-9]+)/social_security_income', views.child_earnings,
        name='child_social_security_income'),
    url(r'^app/children/(?P<child_id>[0-9]+)/parent_social_security_income', views.child_earnings,
        name='parent_social_security_income'),
    url(r'^app/children/(?P<child_id>[0-9]+)/spending_money_income', views.child_earnings,
        name='spending_money_income'),
    url(r'^app/children/(?P<child_id>[0-9]+)/other_friend_income', views.child_earnings,
        name='other_friend_income'),
    url(r'^app/children/(?P<child_id>[0-9]+)/pension_income', views.child_earnings,
        name='pension_income'),
    url(r'^app/children/(?P<child_id>[0-9]+)/annuity_income', views.child_earnings,
        name='annuity_income'),
    url(r'^app/children/(?P<child_id>[0-9]+)/trust_income', views.child_earnings,
        name='trust_income'),
    url(r'^app/children/(?P<child_id>[0-9]+)/other_income', views.child_earnings,
        name='other_income'),
    url(r'^app/adults/$', views.adults, name='adults'),
    url(r'^app/adults/add/$', views.add_adult, name='add_adult'),
    url(r'^app/contact', views.contact, name='contact'),
]