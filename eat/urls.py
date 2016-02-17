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
    url(r'^app/review', views.review, name='review'),
    url(r'^app/assistance_program/participate', views.assistance_program_participate, name='participate'),
    url(r'^app/start_over', views.start_over, name='start_over'),

    # Child URLs
    url(r'^app/children/$', views.children, name='children'),
    url(r'^app/children/add/$', views.add_child, name='add_child'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/edit', views.edit_child, name='edit_child'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/delete', views.delete_child, name='delete_child'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/exempt_child', views.exempt_child, name='exempt_child'),

    #Child earnings
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/salary', views.child_earnings, name='child_salary'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/social_security_income', views.child_earnings,
        name='child_social_security_income'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/parent_social_security_income', views.child_earnings,
        name='parent_social_security_income'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/spending_money_income', views.child_earnings,
        name='spending_money_income'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/other_friend_income', views.child_earnings,
        name='other_friend_income'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/pension_income', views.child_earnings,
        name='pension_income'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/annuity_income', views.child_earnings,
        name='annuity_income'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/trust_income', views.child_earnings,
        name='trust_income'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/other_income', views.child_earnings,
        name='other_income'),

    #Adult URLs
    url(r'^app/adults/$', views.adults, name='adults'),
    url(r'^app/adults/add/$', views.add_adult, name='add_adult'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/edit', views.edit_adult, name='edit_adult'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/delete', views.delete_adult, name='delete_adult'),
    url(r'^app/children/(?P<child_id>[0-9a-z-]+)/salary', views.child_earnings, name='child_salary'),
    url(r'^app/adults/confirm', views.adult_confirm, name='adult_confirm'),

    #Adult earnings
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/salary', views.adult_earnings, name='adult_salary'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/wages', views.adult_earnings, name='adult_wages'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/cash_bonuses', views.adult_earnings, name='cash_bonuses'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/self_employment_income', views.adult_earnings, name='self_employment_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/strike_benefits', views.adult_earnings, name='strike_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/unemployment_insurance', views.adult_earnings, name='unemployment_insurance'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/other_earned_income', views.adult_earnings, name='other_earned_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/are_you_in_military', views.adult_earnings, name='are_you_in_military'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/military_basic_pay', views.adult_earnings, name='military_basic_pay'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/military_bonus', views.adult_earnings, name='military_bonus'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/military_allowance', views.adult_earnings, name='military_allowance'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/military_food', views.adult_earnings, name='military_food'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/military_clothing', views.adult_earnings, name='military_clothing'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/general_assistance', views.adult_earnings, name='general_assistance'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/cash_assistance', views.adult_earnings, name='cash_assistance'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/alimony', views.adult_earnings, name='alimony'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/child_support', views.adult_earnings, name='child_support'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/social_security_income', views.adult_earnings, name='social_security_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/railroad_income', views.adult_earnings, name='railroad_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/pension_income', views.adult_earnings, name='pension_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/annuity_income', views.adult_earnings, name='annuity_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/survivors_benefits', views.adult_earnings, name='survivors_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/ssi_disability_benefits', views.adult_earnings, name='ssi_disability_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/private_disability_benefits', views.adult_earnings, name='private_disability_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/black_lung_benefits', views.adult_earnings, name='black_lung_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/workers_compensation', views.adult_earnings, name='workers_compensation'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/veterans_benefits', views.adult_earnings, name='veterans_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/other_retirement_sources', views.adult_earnings, name='other_retirement_sources'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/interest_income', views.adult_earnings, name='interest_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/investment_income', views.adult_earnings, name='investment_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/dividends', views.adult_earnings, name='dividends'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/trust_or_estates_income', views.adult_earnings, name='trust_or_estates_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/rental_income', views.adult_earnings, name='rental_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/royalties_income', views.adult_earnings, name='royalties_income'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/prize_winnings', views.adult_earnings, name='prize_winnings'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/savings_withdrawn', views.adult_earnings, name='savings_withdrawn'),
    url(r'^app/adults/(?P<adult_id>[0-9a-z-]+)/cash_gifts', views.adult_earnings, name='cash_gifts'),


    #Contacts
    url(r'^app/contact', views.contact, name='contact'),
    url(r'^app/race', views.race, name='race'),

    #Admin
    url(r'^admin/dashboard', views.admin_dashboard, name='admin_dashboard'),
    url(r'^admin/applications/$', views.admin_applications, name='admin_applications'),
    url(r'^admin/applications/foster_child/', views.admin_applications_foster_child,
        name='admin_applications_foster_child'),
    url(r'^admin/applications/assistance_program/', views.admin_applications_assistance_program,
        name='admin_applications_assistance_program'),

    url(r'^admin/applications/export/', views.admin_applications_export,
        name='admin_applications_export'),
    url(r'^admin/applications/children/export/', views.admin_children_export,
        name='admin_children_export'),
    url(r'^admin/applications/adults/export/', views.admin_adults_export,
        name='admin_adults_export'),

    url(r'^admin/application/(?P<application_id>[0-9a-z-]+)', views.admin_application_view,
        name='admin_application_view'),
    url(r'^admin/users', views.admin_users, name='admin_users'),

]