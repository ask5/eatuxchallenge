from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from eat.models import Application, Child, Adult
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = "Password must contain at least 8 characters."
        self.fields['password2'].label = "Confirm Password"
        self.fields['email'].label = "Email"

    def clean_email(self):
        qs = User.objects.filter(email=self.cleaned_data['email'])
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.count():
            raise forms.ValidationError('That email address is already in use')
        else:
            return self.cleaned_data['email']


class AssistanceProgramForm(ModelForm):
    def clean_case_number(self):
        if self.cleaned_data['assistance_program'] and self.cleaned_data['case_number'] == '':
            raise forms.ValidationError('Case number is mandatory if you are currently participating in an assistance'
                                        ' program')
        else:
            return self.cleaned_data['case_number']

    class Meta:
        model = Application
        fields = ['assistance_program', 'case_number']
        widgets = {
            'assistance_program': forms.RadioSelect
        }
        labels = {
            'assistance_program': "Participate in any Assistance Program?"
        }
        help_texts = {
            'case_number': "Provide case number if you participate."
        }


class AddChildForm(ModelForm):

    class Meta:
        model = Child
        fields = ['first_name', 'middle_name', 'last_name', 'is_student', 'foster_child', 'hmr']
        exclude = ("application",)
        widgets = {
            'is_student': forms.CheckboxInput,
            'foster_child': forms.CheckboxInput,
            'hmr': forms.CheckboxInput
        }
        labels = {
            'is_student': "Is this child a student?",
            'foster_child': "Is this a foster child?",
            'hmr': "Is the child Homeless, Migrant or Runaway?",
        }


class ChildSalaryForm(ModelForm):

    def save(self, commit=True):
        instance = super(ChildSalaryForm, self).save(commit=False)
        if not instance.salary:
            instance.salary = 0
            instance.salary_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Child
        fields = ['salary', 'salary_frequency']
        widgets = {
            'salary_frequency': forms.RadioSelect
        }
        labels = {
            'salary': "Earnings $",
            'salary_frequency': "How often?"
        }


class ChildSocialSecurityForm(ModelForm):

    def save(self, commit=True):
        instance = super(ChildSocialSecurityForm, self).save(commit=False)
        if not instance.ssi_disability:
            instance.ssi_disability = 0
            instance.ssi_disability_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Child
        fields = ['ssi_disability', 'ssi_disability_frequency']
        widgets = {
            'ssi_disability_frequency': forms.RadioSelect
        }
        labels = {
            'ssi_disability': "Earnings $",
            'ssi_disability_frequency': "How often?"
        }


class ParentSocialSecurityForm(ModelForm):

    def save(self, commit=True):
        instance = super(ParentSocialSecurityForm, self).save(commit=False)
        if not instance.ssi_parent_disability:
            instance.ssi_parent_disability = 0
            instance.ssi_parent_disability_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Child
        fields = ['ssi_parent_disability', 'ssi_parent_disability_frequency']
        widgets = {
            'ssi_parent_disability_frequency': forms.RadioSelect
        }
        labels = {
            'ssi_parent_disability': "Earnings $",
            'ssi_parent_disability_frequency': "How often?"
        }


class ChildSpendingMoneyForm(ModelForm):

    def save(self, commit=True):
        instance = super(ChildSpendingMoneyForm, self).save(commit=False)
        if not instance.spending_money_income:
            instance.spending_money_income = 0
            instance.spending_money_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Child
        fields = ['spending_money_income', 'spending_money_income_frequency']
        widgets = {
            'spending_money_income_frequency': forms.RadioSelect
        }
        labels = {
            'spending_money_income': "Earnings $",
            'spending_money_income_frequency': "How often?"
        }


class ChildOtherFriendIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(ChildOtherFriendIncomeForm, self).save(commit=False)
        if not instance.other_friend_income:
            instance.other_friend_income = 0
            instance.other_friend_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Child
        fields = ['other_friend_income', 'other_friend_income_frequency']
        widgets = {
            'other_friend_income_frequency': forms.RadioSelect
        }
        labels = {
            'other_friend_income': "Earnings $",
            'other_friend_income_frequency': "How often?"
        }


class ChildPensionIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(ChildPensionIncomeForm, self).save(commit=False)
        if not instance.pension_income:
            instance.pension_income = 0
            instance.pension_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Child
        fields = ['pension_income', 'pension_income_frequency']
        widgets = {
            'pension_income_frequency': forms.RadioSelect
        }
        labels = {
            'pension_income': "Earnings $",
            'pension_income_frequency': "How often?"
        }


class ChildAnnuityIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(ChildAnnuityIncomeForm, self).save(commit=False)
        if not instance.annuity_income:
            instance.annuity_income = 0
            instance.annuity_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Child
        fields = ['annuity_income', 'annuity_income_frequency']
        widgets = {
            'annuity_income_frequency': forms.RadioSelect
        }
        labels = {
            'annuity_income': "Earnings $",
            'annuity_income_frequency': "How often?"
        }


class ChildTrustIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(ChildTrustIncomeForm, self).save(commit=False)
        if not instance.trust_income:
            instance.trust_income = 0
            instance.trust_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Child
        fields = ['trust_income', 'trust_income_frequency']
        widgets = {
            'trust_income_frequency': forms.RadioSelect
        }
        labels = {
            'trust_income': "Earnings $",
            'trust_income_frequency': "How often?"
        }


class ChildOtherIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(ChildOtherIncomeForm, self).save(commit=False)
        if not instance.other_income:
            instance.other_income = 0
            instance.other_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Child
        fields = ['other_income', 'other_income_frequency']
        widgets = {
            'other_income_frequency': forms.RadioSelect
        }
        labels = {
            'other_income': "Earnings $",
            'other_income_frequency': "How often?"
        }

class AddAdultForm(ModelForm):

    class Meta:
        model = Adult
        fields = ['first_name', 'middle_name', 'last_name']
        exclude = ("application",)


class AdultSalaryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AdultSalaryForm, self).__init__(*args, **kwargs)
        self.fields['salary_frequency'].empty_label = None

    def save(self, commit=True):
        instance = super(AdultSalaryForm, self).save(commit=False)
        if not instance.salary:
            instance.salary = 0
            instance.salary_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['salary', 'salary_frequency']
        widgets = {
            'salary_frequency': forms.RadioSelect
        }
        labels = {
            'salary': "Earnings $",
            'salary_frequency': "How often?"
        }


class AdultWagesForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultWagesForm, self).save(commit=False)
        if not instance.wages:
            instance.wages = 0
            instance.wages_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['wages', 'wages_frequency']
        widgets = {
            'wages_frequency': forms.RadioSelect
        }
        labels = {
            'wages': "Earnings $",
            'wages_frequency': "How often?"
        }


class AdultCashBonusForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultCashBonusForm, self).save(commit=False)
        if not instance.cash_bonuses:
            instance.cash_bonuses = 0
            instance.cash_bonuses_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['cash_bonuses', 'cash_bonuses_frequency']
        widgets = {
            'cash_bonuses_frequency': forms.RadioSelect
        }
        labels = {
            'cash_bonuses': "Earnings $",
            'cash_bonuses_frequency': "How often?"
        }


class AdultSelfEmploymentForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultSelfEmploymentForm, self).save(commit=False)
        if not instance.self_employment_income:
            instance.self_employment_income = 0
            instance.self_employment_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['self_employment_income', 'self_employment_income_frequency']
        widgets = {
            'self_employment_income_frequency': forms.RadioSelect
        }
        labels = {
            'self_employment_income': "Earnings $",
            'self_employment_income_frequency': "How often?"
        }


class AdultStrikeBenefitsForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultStrikeBenefitsForm, self).save(commit=False)
        if not instance.strike_benefits:
            instance.strike_benefits = 0
            instance.strike_benefits_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['strike_benefits', 'strike_benefits_frequency']
        widgets = {
            'strike_benefits_frequency': forms.RadioSelect
        }
        labels = {
            'strike_benefits_income': "Earnings $",
            'strike_benefits_frequency': "How often?"
        }


class AdultUnemploymentInsuranceForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultUnemploymentInsuranceForm, self).save(commit=False)
        if not instance.unemployment_insurance:
            instance.unemployment_insurance = 0
            instance.unemployment_insurance_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['unemployment_insurance', 'unemployment_insurance_frequency']
        widgets = {
            'unemployment_insurance_frequency': forms.RadioSelect
        }
        labels = {
            'unemployment_insurance': "Earnings $",
            'unemployment_insurance_frequency': "How often?"
        }


class AdultOtherEarnedIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultOtherEarnedIncomeForm, self).save(commit=False)
        if not instance.other_earned_income:
            instance.other_earned_income = 0
            instance.other_earned_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['other_earned_income', 'other_earned_income_frequency']
        widgets = {
            'other_earned_income_frequency': forms.RadioSelect
        }
        labels = {
            'other_earned_income': "Earnings $",
            'other_earned_income_frequency': "How often?"
        }


class AdultMilitaryBasicPayForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultMilitaryBasicPayForm, self).save(commit=False)
        if not instance.military_basic_pay:
            instance.military_basic_pay = 0
            instance.military_basic_pay_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['military_basic_pay', 'military_basic_pay_frequency']
        widgets = {
            'military_basic_pay_frequency': forms.RadioSelect
        }
        labels = {
            'military_basic_pay': "Earnings $",
            'military_basic_pay_frequency': "How often?"
        }


class AdultMilitaryBonusForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultMilitaryBonusForm, self).save(commit=False)
        if not instance.military_bonus:
            instance.military_bonus = 0
            instance.military_bonus_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['military_bonus', 'military_bonus_frequency']
        widgets = {
            'military_bonus_frequency': forms.RadioSelect
        }
        labels = {
            'military_bonus': "Earnings $",
            'military_bonus_frequency': "How often?"
        }


class AdultMilitaryAllowanceForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultMilitaryAllowanceForm, self).save(commit=False)
        if not instance.military_allowance:
            instance.military_allowance = 0
            instance.military_allowance_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['military_allowance', 'military_allowance_frequency']
        widgets = {
            'military_allowance_frequency': forms.RadioSelect
        }
        labels = {
            'military_allowance': "Earnings $",
            'military_allowance_frequency': "How often?"
        }


class AdultMilitaryFoodForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultMilitaryFoodForm, self).save(commit=False)
        if not instance.military_food:
            instance.military_food = 0
            instance.military_food_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['military_food', 'military_food_frequency']
        widgets = {
            'military_food_frequency': forms.RadioSelect
        }
        labels = {
            'military_food': "Earnings $",
            'military_food_frequency': "How often?"
        }


class AdultMilitaryClothingForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultMilitaryClothingForm, self).save(commit=False)
        if not instance.military_clothing:
            instance.military_clothing = 0
            instance.military_clothing_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['military_clothing', 'military_clothing_frequency']
        widgets = {
            'military_clothing_frequency': forms.RadioSelect
        }
        labels = {
            'military_clothing': "Earnings $",
            'military_clothing_frequency': "How often?"
        }


class AdultGeneralAssistanceForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultGeneralAssistanceForm, self).save(commit=False)
        if not instance.general_assistance:
            instance.general_assistance = 0
            instance.general_assistance_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['general_assistance', 'general_assistance_frequency']
        widgets = {
            'general_assistance_frequency': forms.RadioSelect
        }
        labels = {
            'general_assistance': "Earnings $",
            'general_assistance_frequency': "How often?"
        }


class AdultOtherAssistanceForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultOtherAssistanceForm, self).save(commit=False)
        if not instance.other_assistance:
            instance.other_assistance = 0
            instance.other_assistance_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['other_assistance', 'other_assistance_frequency']
        widgets = {
            'other_assistance_frequency': forms.RadioSelect
        }
        labels = {
            'other_assistance': "Earnings $",
            'other_assistance_frequency': "How often?"
        }


class AdultAlimonyForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultAlimonyForm, self).save(commit=False)
        if not instance.alimony:
            instance.alimony = 0
            instance.alimony_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['alimony', 'alimony_frequency']
        widgets = {
            'alimony_frequency': forms.RadioSelect
        }
        labels = {
            'alimony': "Earnings $",
            'alimony_frequency': "How often?"
        }


class AdultChildSupportForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultChildSupportForm, self).save(commit=False)
        if not instance.child_support:
            instance.child_support = 0
            instance.child_support_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['child_support', 'child_support_frequency']
        widgets = {
            'child_support_frequency': forms.RadioSelect
        }
        labels = {
            'child_support': "Earnings $",
            'child_support_frequency': "How often?"
        }


class AdultSocialSecurityIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultSocialSecurityIncomeForm, self).save(commit=False)
        if not instance.social_security_income:
            instance.social_security_income = 0
            instance.social_security_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['social_security_income', 'social_security_income_frequency']
        widgets = {
            'social_security_income_frequency': forms.RadioSelect
        }
        labels = {
            'social_security_income': "Earnings $",
            'social_security_income_frequency': "How often?"
        }


class AdultRailroadIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultRailroadIncomeForm, self).save(commit=False)
        if not instance.railroad_income:
            instance.railroad_income = 0
            instance.railroad_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['railroad_income', 'railroad_income_frequency']
        widgets = {
            'railroad_income_frequency': forms.RadioSelect
        }
        labels = {
            'railroad_income': "Earnings $",
            'railroad_income_frequency': "How often?"
        }


class AdultPensionIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultPensionIncomeForm, self).save(commit=False)
        if not instance.pension_income:
            instance.pension_income = 0
            instance.pension_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['pension_income', 'pension_income_frequency']
        widgets = {
            'pension_income_frequency': forms.RadioSelect
        }
        labels = {
            'pension_income': "Earnings $",
            'pension_income_frequency': "How often?"
        }


class AdultAnnuityIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultAnnuityIncomeForm, self).save(commit=False)
        if not instance.annuity_income:
            instance.annuity_income = 0
            instance.annuity_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['annuity_income', 'annuity_income_frequency']
        widgets = {
            'annuity_income_frequency': forms.RadioSelect
        }
        labels = {
            'annuity_income': "Earnings $",
            'annuity_income_frequency': "How often?"
        }


class AdultSurvivorsBenefitsForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultSurvivorsBenefitsForm, self).save(commit=False)
        if not instance.survivors_benefits:
            instance.survivors_benefits = 0
            instance.survivors_benefits_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['survivors_benefits', 'survivors_benefits_frequency']
        widgets = {
            'survivors_benefits_frequency': forms.RadioSelect
        }
        labels = {
            'survivors_benefits': "Earnings $",
            'survivors_benefits_frequency': "How often?"
        }


class AdultSSIBenefitsForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultSSIBenefitsForm, self).save(commit=False)
        if not instance.ssi_disability_benefits:
            instance.ssi_disability_benefits = 0
            instance.ssi_disability_benefits_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['ssi_disability_benefits', 'ssi_disability_benefits_frequency']
        widgets = {
            'ssi_disability_benefits_frequency': forms.RadioSelect
        }
        labels = {
            'ssi_disability_benefits': "Earnings $",
            'ssi_disability_benefits_frequency': "How often?"
        }


class AdultPrivateDisabilityBenefitsForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultPrivateDisabilityBenefitsForm, self).save(commit=False)
        if not instance.private_disability_benefits:
            instance.private_disability_benefits = 0
            instance.private_disability_benefits_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['private_disability_benefits', 'private_disability_benefits_frequency']
        widgets = {
            'private_disability_benefits_frequency': forms.RadioSelect
        }
        labels = {
            'private_disability_benefits': "Earnings $",
            'private_disability_benefits_frequency': "How often?"
        }


class AdultBlackLungBenefitsForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultBlackLungBenefitsForm, self).save(commit=False)
        if not instance.black_lung_benefits:
            instance.black_lung_benefits = 0
            instance.black_lung_benefits_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['black_lung_benefits', 'black_lung_benefits_frequency']
        widgets = {
            'black_lung_benefits_frequency': forms.RadioSelect
        }
        labels = {
            'black_lung_benefits': "Earnings $",
            'black_lung_benefits_frequency': "How often?"
        }


class AdultWorkersCompensationForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultWorkersCompensationForm, self).save(commit=False)
        if not instance.workers_compensation:
            instance.workers_compensation = 0
            instance.workers_compensation_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['workers_compensation', 'workers_compensation_frequency']
        widgets = {
            'workers_compensation_frequency': forms.RadioSelect
        }
        labels = {
            'workers_compensation': "Earnings $",
            'workers_compensation_frequency': "How often?"
        }


class AdultVeteransBenefitsForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultVeteransBenefitsForm, self).save(commit=False)
        if not instance.veterans_benefits:
            instance.veterans_benefits = 0
            instance.veterans_benefits_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['veterans_benefits', 'veterans_benefits_frequency']
        widgets = {
            'veterans_benefits_frequency': forms.RadioSelect
        }
        labels = {
            'veterans_benefits': "Earnings $",
            'veterans_benefits_frequency': "How often?"
        }


class AdultOtherRetirementSourcesForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultOtherRetirementSourcesForm, self).save(commit=False)
        if not instance.other_retirement_sources:
            instance.other_retirement_sources = 0
            instance.other_retirement_sources_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['other_retirement_sources', 'other_retirement_sources_frequency']
        widgets = {
            'other_retirement_sources_frequency': forms.RadioSelect
        }
        labels = {
            'other_retirement_sources': "Earnings $",
            'other_retirement_sources_frequency': "How often?"
        }


class AdultInterestIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultInterestIncomeForm, self).save(commit=False)
        if not instance.interest_income:
            instance.interest_income = 0
            instance.interest_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['interest_income', 'interest_income_frequency']
        widgets = {
            'interest_income_frequency': forms.RadioSelect
        }
        labels = {
            'interest_income_sources': "Earnings $",
            'interest_income_frequency': "How often?"
        }


class AdultDividendsForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultDividendsForm, self).save(commit=False)
        if not instance.dividends:
            instance.dividends = 0
            instance.dividends_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['dividends', 'dividends_frequency']
        widgets = {
            'dividends_frequency': forms.RadioSelect
        }
        labels = {
            'dividends_sources': "Earnings $",
            'dividends_frequency': "How often?"
        }


class AdultTrustOrEstatesIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultTrustOrEstatesIncomeForm, self).save(commit=False)
        if not instance.trust_or_estates_income:
            instance.trust_or_estates_income = 0
            instance.trust_or_estates_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['trust_or_estates_income', 'trust_or_estates_income_frequency']
        widgets = {
            'trust_or_estates_income_frequency': forms.RadioSelect
        }
        labels = {
            'trust_or_estates_income': "Earnings $",
            'trust_or_estates_income_frequency': "How often?"
        }


class AdultRentalIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultRentalIncomeForm, self).save(commit=False)
        if not instance.rental_income:
            instance.rental_income = 0
            instance.rental_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['rental_income', 'rental_income_frequency']
        widgets = {
            'rental_income_frequency': forms.RadioSelect
        }
        labels = {
            'rental_income': "Earnings $",
            'rental_income_frequency': "How often?"
        }


class AdultRoyaltiesIncomeForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultRoyaltiesIncomeForm, self).save(commit=False)
        if not instance.royalties_income:
            instance.royalties_income = 0
            instance.royalties_income_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['royalties_income', 'royalties_income_frequency']
        widgets = {
            'royalties_income_frequency': forms.RadioSelect
        }
        labels = {
            'royalties_income': "Earnings $",
            'royalties_income_frequency': "How often?"
        }


class AdultPrizeWinningsForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultPrizeWinningsForm, self).save(commit=False)
        if not instance.prize_winnings:
            instance.prize_winnings = 0
            instance.prize_winnings_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['prize_winnings', 'prize_winnings_frequency']
        widgets = {
            'prize_winnings_frequency': forms.RadioSelect
        }
        labels = {
            'prize_winnings': "Earnings $",
            'prize_winnings_frequency': "How often?"
        }


class AdultSavingsWithdrawnForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultSavingsWithdrawnForm, self).save(commit=False)
        if not instance.savings_withdrawn:
            instance.savings_withdrawn = 0
            instance.savings_withdrawn_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['savings_withdrawn', 'savings_withdrawn_frequency']
        widgets = {
            'savings_withdrawn_frequency': forms.RadioSelect
        }
        labels = {
            'savings_withdrawn': "Earnings $",
            'savings_withdrawn_frequency': "How often?"
        }


class AdultCashGiftsForm(ModelForm):

    def save(self, commit=True):
        instance = super(AdultCashGiftsForm, self).save(commit=False)
        if not instance.cash_gifts:
            instance.cash_gifts = 0
            instance.cash_gifts_frequency = None
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Adult
        fields = ['cash_gifts', 'cash_gifts_frequency']
        widgets = {
            'cash_gifts_frequency': forms.RadioSelect
        }
        labels = {
            'cash_gifts': "Earnings $",
            'cash_gifts_frequency': "How often?"
        }
