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