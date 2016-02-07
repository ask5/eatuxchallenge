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
    url(r'^app/assistance_program/$', views.assistance_program, name='assistance_program'),
    url(r'^app/assistance_program/confirm', views.confirm_assistance_program, name='confirm_assistance_program'),


    # Child URLs
    url(r'^app/children/$', views.children, name='children'),
    url(r'^app/children/add/$', views.add_child, name='add_child'),
    url(r'^app/children/(?P<child_id>[0-9]+)/edit', views.edit_child, name='edit_child'),
    url(r'^app/children/(?P<child_id>[0-9]+)/delete', views.delete_child, name='delete_child'),
    url(r'^app/children/(?P<child_id>[0-9]+)/exempt_child', views.exempt_child, name='exempt_child'),

    #Child earnings
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

    #Adult URLs
    url(r'^app/adults/$', views.adults, name='adults'),
    url(r'^app/adults/add/$', views.add_adult, name='add_adult'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/edit', views.edit_adult, name='edit_adult'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/delete', views.delete_adult, name='delete_adult'),
    url(r'^app/children/(?P<child_id>[0-9]+)/salary', views.child_earnings, name='child_salary'),

    #Adult earnings
    url(r'^app/adults/(?P<adult_id>[0-9]+)/salary', views.adult_earnings, name='adult_salary'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/wages', views.adult_earnings, name='adult_wages'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/cash_bonuses', views.adult_earnings, name='cash_bonuses'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/self_employment_income', views.adult_earnings, name='self_employment_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/strike_benefits', views.adult_earnings, name='strike_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/unemployment_insurance', views.adult_earnings, name='unemployment_insurance'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/other_earned_income', views.adult_earnings, name='other_earned_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/are_you_in_military', views.adult_earnings, name='are_you_in_military'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/military_basic_pay', views.adult_earnings, name='military_basic_pay'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/military_bonus', views.adult_earnings, name='military_bonus'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/military_allowance', views.adult_earnings, name='military_allowance'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/military_food', views.adult_earnings, name='military_food'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/military_clothing', views.adult_earnings, name='military_clothing'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/general_assistance', views.adult_earnings, name='general_assistance'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/cash_assistance', views.adult_earnings, name='cash_assistance'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/alimony', views.adult_earnings, name='alimony'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/child_support', views.adult_earnings, name='child_support'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/social_security_income', views.adult_earnings, name='social_security_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/railroad_income', views.adult_earnings, name='railroad_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/pension_income', views.adult_earnings, name='pension_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/annuity_income', views.adult_earnings, name='annuity_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/survivors_benefits', views.adult_earnings, name='survivors_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/ssi_disability_benefits', views.adult_earnings, name='ssi_disability_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/private_disability_benefits', views.adult_earnings, name='private_disability_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/black_lung_benefits', views.adult_earnings, name='black_lung_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/workers_compensation', views.adult_earnings, name='workers_compensation'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/veterans_benefits', views.adult_earnings, name='veterans_benefits'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/other_retirement_sources', views.adult_earnings, name='other_retirement_sources'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/interest_income', views.adult_earnings, name='interest_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/investment_income', views.adult_earnings, name='investment_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/dividends', views.adult_earnings, name='dividends'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/trust_or_estates_income', views.adult_earnings, name='trust_or_estates_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/rental_income', views.adult_earnings, name='rental_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/royalties_income', views.adult_earnings, name='royalties_income'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/prize_winnings', views.adult_earnings, name='prize_winnings'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/savings_withdrawn', views.adult_earnings, name='savings_withdrawn'),
    url(r'^app/adults/(?P<adult_id>[0-9]+)/cash_gifts', views.adult_earnings, name='cash_gifts'),


    #Contacts
    url(r'^app/contact', views.contact, name='contact'),
]