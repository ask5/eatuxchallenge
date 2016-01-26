from eat.models import Application
from django.core.urlresolvers import resolve
from  eat.forms import *


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

class EarningsForms(object):
    """
    form factory for child earninigs pages
    """
    @classmethod
    def get_form(cls, page_name, instance, data=None):

        if page_name == "child_salary":
            return ChildSalaryForm(data=data, instance=instance)

        if page_name == "child_social_security_income":
            return ChildSocialSecurityForm(data=data, instance=instance)

        if page_name == "parent_social_security_income":
            return ParentSocialSecurityForm(data=data, instance=instance)

        if page_name == "spending_money_income":
            return ChildSpendingMoneyForm(data=data, instance=instance)

        if page_name == "other_friend_income":
            return ChildOtherFriendIncomeForm(data=data, instance=instance)

        if page_name == "pension_income":
            return ChildPensionIncomeForm(data=data, instance=instance)

        if page_name == "annuity_income":
            return ChildAnnuityIncomeForm(data=data, instance=instance)

        if page_name == "trust_income":
            return ChildTrustIncomeForm(data=data, instance=instance)

        if page_name == "other_income":
            return ChildOtherIncomeForm(data=data, instance=instance)