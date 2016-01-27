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

class ChildEarningsFormsFactory(object):
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


class AdultEarningsFormsFactory(object):
    """
    form factory for adult earninigs pages
    """
    @classmethod
    def get_form(cls, page_name, instance, data=None):

        if page_name == "adult_salary":
            return AdultSalaryForm(data=data, instance=instance)

        if page_name == "adult_wages":
            return AdultWagesForm(data=data, instance=instance)

        if page_name == "cash_bonuses":
            return AdultCashBonusForm(data=data, instance=instance)

        if page_name == "self_employment_income":
            return AdultSelfEmploymentForm(data=data, instance=instance)

        if page_name == "strike_benefits":
            return AdultStrikeBenefitsForm(data=data, instance=instance)

        if page_name == "unemployment_insurance":
            return AdultUnemploymentInsuranceForm(data=data, instance=instance)

        if page_name == "other_earned_income":
            return AdultOtherEarnedIncomeForm(data=data, instance=instance)

        if page_name == "military_basic_pay":
            return AdultMilitaryBasicPayForm(data=data, instance=instance)

        if page_name == "military_bonus":
            return AdultMilitaryBonusForm(data=data, instance=instance)

        if page_name == "military_allowance":
            return AdultMilitaryAllowanceForm(data=data, instance=instance)

        if page_name == "military_food":
            return AdultMilitaryFoodForm(data=data, instance=instance)

        if page_name == "military_clothing":
            return AdultMilitaryClothingForm(data=data, instance=instance)

        if page_name == "general_assistance":
            return AdultGeneralAssistanceForm(data=data, instance=instance)

        if page_name == "other_assistance":
            return AdultOtherAssistanceForm(data=data, instance=instance)

        if page_name == "alimony":
            return AdultAlimonyForm(data=data, instance=instance)

        if page_name == "child_support":
            return AdultChildSupportForm(data=data, instance=instance)

        if page_name == "social_security_income":
            return AdultSocialSecurityIncomeForm(data=data, instance=instance)

        if page_name == "railroad_income":
            return AdultRailroadIncomeForm(data=data, instance=instance)

        if page_name == "pension_income":
            return AdultPensionIncomeForm(data=data, instance=instance)

        if page_name == "annuity_income":
            return AdultAnnuityIncomeForm(data=data, instance=instance)

        if page_name == "survivors_benefits":
            return AdultSurvivorsBenefitsForm(data=data, instance=instance)

        if page_name == "ssi_disability_benefits":
            return AdultSSIBenefitsForm(data=data, instance=instance)

        if page_name == "private_disability_benefits":
            return AdultPrivateDisabilityBenefitsForm(data=data, instance=instance)

        if page_name == "black_lung_benefits":
            return AdultBlackLungBenefitsForm(data=data, instance=instance)

        if page_name == "workers_compensation":
            return AdultWorkersCompensationForm(data=data, instance=instance)

        if page_name == "veterans_benefits":
            return AdultVeteransBenefitsForm(data=data, instance=instance)

        if page_name == "other_retirement_sources":
            return AdultOtherRetirementSourcesForm(data=data, instance=instance)

        if page_name == "interest_income":
            return AdultInterestIncomeForm(data=data, instance=instance)

        if page_name == "dividends":
            return AdultDividendsForm(data=data, instance=instance)

        if page_name == "trust_or_estates_income":
            return AdultTrustOrEstatesIncomeForm(data=data, instance=instance)

        if page_name == "rental_income":
            return AdultRentalIncomeForm(data=data, instance=instance)

        if page_name == "royalties_income":
            return AdultRoyaltiesIncomeForm(data=data, instance=instance)

        if page_name == "prize_winnings":
            return AdultPrizeWinningsForm(data=data, instance=instance)

        if page_name == "savings_withdrawn":
            return AdultSavingsWithdrawnForm(data=data, instance=instance)

        if page_name == "cash_gifts":
            return AdultCashGiftsForm(data=data, instance=instance)
