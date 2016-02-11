from eat.models import EarningsPage
from django.core.urlresolvers import resolve
from eat.forms import *
from . import *

class AppUtil(object):

    @classmethod
    def get(cls, id):
        return Application.applications.get(pk=id)

    @classmethod
    def get_by_user(cls, user):
        app = Application.applications.filter(user=user.id)
        return app

    @classmethod
    def set_last_page(cls, app, path):
        app.last_page = path
        app.save()

    @classmethod
    def get_earnings_pages(self, entity):
        p = EarningsPage.objects.get(name=entity)
        e = []
        while p.next.name != entity:
            if p.next.page_type == 'form':
                e.append(p.next)
            p = p.next
        return e

    @classmethod
    def get_nav(cls, nav, url):
        t = []
        for k, v in nav.items():
            v['current'] = True if v['url'] == url else False
            t.append(v)
        s = sorted(t, key=lambda k:k['position'])
        return s

    @classmethod
    def get_child_total_earning(cls, child):
        t = 0
        t += child.salary
        t += child.ssi_disability
        t += child.ssi_parent_disability
        t += child.spending_money_income
        t += child.other_friend_income
        t += child.pension_income
        t += child.annuity_income
        t += child.trust_income
        t += child.other_income
        return t

    @classmethod
    def get_adult_total_earning(cls, adult):
        t = 0
        t += adult.salary
        t += adult.wages
        t += adult.cash_bonuses
        t += adult.self_employment_income
        t += adult.strike_benefits
        t += adult.unemployment_insurance
        t += adult.other_earned_income
        t += adult.military_basic_pay
        t += adult.military_bonus
        t += adult.military_allowance
        t += adult.military_food
        t += adult.military_clothing
        t += adult.general_assistance
        t += adult.cash_assistance
        t += adult.alimony
        t += adult.child_support
        t += adult.social_security_income
        t += adult.railroad_income
        t += adult.pension_income
        t += adult.annuity_income
        t += adult.survivors_benefits
        t += adult.ssi_disability_benefits
        t += adult.private_disability_benefits
        t += adult.black_lung_benefits
        t += adult.workers_compensation
        t += adult.veterans_benefits
        t += adult.other_retirement_sources
        t += adult.interest_income
        t += adult.investment_income
        t += adult.dividends
        t += adult.trust_or_estates_income
        t += adult.rental_income
        t += adult.royalties_income
        t += adult.prize_winnings
        t += adult.savings_withdrawn
        t += adult.cash_gifts
        return t