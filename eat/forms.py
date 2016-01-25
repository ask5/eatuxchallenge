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