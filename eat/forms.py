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
        self.fields['username'].error_messages = { 'required': 'Username cannot be blank' }
        self.fields['password1'].help_text = None
        self.fields['password1'].error_messages = { 'required': 'Password cannot be blank' }
        self.fields['password2'].help_text = "Password must contain at least 8 characters."
        self.fields['password2'].label = "Confirm Password"
        self.fields['password2'].error_messages = { 'required': 'Retype the password for confirmation' }
        self.fields['email'].label = "Email"


    def clean_email(self):
        e = self.cleaned_data['email']
        if e == '':
            raise forms.ValidationError('Email cannot be blank')
        else:
            qs = User.objects.filter(email=e)
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

    def clean(self):
        cleaned_data = super(AddChildForm, self).clean()
        fname = cleaned_data.get("first_name")
        lname = cleaned_data.get("last_name")
        if Child.children.filter(first_name=fname, last_name=lname).exists():
            raise forms.ValidationError("Child with the same name already exits")
        else:
            return cleaned_data



class AddAdultForm(ModelForm):

    class Meta:
        model = Adult
        fields = ['first_name', 'middle_name', 'last_name']
        exclude = ("application",)


class EarningsForm(forms.Form):

    PAY_FREQUENCIES = (
        (1, 'Weekly'),
        (2, 'Bi-Weekly'),
        (3, '2x Month'),
        (4, 'Monthly')
    )

    earning = forms.IntegerField(label="Earnings $", required=False)
    frequency = forms.ChoiceField(choices=PAY_FREQUENCIES, label="How often?", widget=forms.RadioSelect, required=False)

    def clean_frequency(self):
        if self.cleaned_data['earning'] is not None and self.cleaned_data['earning'] != 0\
                and self.cleaned_data['frequency'] == "":
            raise forms.ValidationError("Please specify how often you get the earnings")
        else:
            return self.cleaned_data['frequency']


class ContactForm(ModelForm):

    class Meta:
        model = Application
        fields = ('street_address', 'apt', 'city', 'state', 'zip', 'phone', 'email',
                  'first_name', 'last_name', 'signature')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['state'].empty_label = "Select a State"
        self.fields['state'].widget.choices = self.fields['state'].choices