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
        if self.cleaned_data['case_number'] == '':
            raise forms.ValidationError('Case number is mandatory if you are currently participating in an assistance'
                                        ' program')
        else:
            return self.cleaned_data['case_number']

    class Meta:
        model = Application
        fields = ['assistance_program', 'case_number']


class FosterChildForm(ModelForm):
    delete = forms.BooleanField()

    class Meta:
        model = Application
        fields = ['app_for_foster_child']

    def clean(self):
        cleaned_data = super(FosterChildForm, self).clean()
        if 'delete' in self.cleaned_data:
            delete = self.cleaned_data['delete']
        else:
            delete = False

        if Child.children.filter(application=self.instance).exists() and not delete:
            raise forms.ValidationError("Already existing child information will be deleted.")
        else:
            return cleaned_data


class RaceForm(ModelForm):
    class Meta:
        model = Application
        fields = ['ethnicity', 'is_american_indian', 'is_asian', 'is_black', 'is_hawaiian', 'is_white']
        widgets = {
            'ethnicity': forms.RadioSelect(),
            'is_american_indian': forms.CheckboxInput,
            'is_asian': forms.CheckboxInput,
            'is_black': forms.CheckboxInput,
            'is_hawaiian': forms.CheckboxInput,
            'is_white': forms.CheckboxInput
        }

class AddChildForm(ModelForm):

    class Meta:
        model = Child
        fields = ['first_name', 'middle_name', 'last_name', 'is_student', 'foster_child', 'hmr',
                  'is_head_start_participant']
        exclude = ("application",)
        widgets = {
            'is_student': forms.CheckboxInput,
            'foster_child': forms.CheckboxInput,
            'hmr': forms.CheckboxInput,
            'is_head_start_participant': forms.CheckboxInput
        }
        labels = {
            'is_student': "Is this child a student?",
            'foster_child': "Is this a foster child?",
            'hmr': "Is the child Homeless, Migrant or Runaway?",
            'is_head_start_participant': "Is the child Head Start participant?",
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

    todays_date = forms.DateField(('%m/%d/%Y',), label='Today''s Date', required=True,
        widget=forms.DateTimeInput(format='%m/%d/%Y', attrs={
            'class':'input',
            'readonly':'readonly',
            'size':'15'
        })
    )

    class Meta:
        model = Application
        fields = ('street_address', 'apt', 'city', 'state', 'zip', 'phone', 'email',
                  'first_name', 'last_name', 'signature', 'ssn_four_digit', 'no_ssn', 'todays_date')

        widgets = {
            'todays_date': forms.DateInput(format='%m/%d/%Y')
        }

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        fname = cleaned_data.get("first_name")
        lname = cleaned_data.get("last_name")
        street_address = cleaned_data.get("street_address")
        signature = cleaned_data.get("signature")
        city = cleaned_data.get("city")
        state = cleaned_data.get("state")
        zip = cleaned_data.get("zip")
        tdate = cleaned_data.get("todays_date")
        errors = []

        if fname == '' or lname == '':
            errors.append(forms.ValidationError("Enter both first and last name"))

        if street_address == '' or city == '' or state == '' or zip == '':
            errors.append(forms.ValidationError("Enter complete address"))

        if not self.cleaned_data['no_ssn'] and not self.cleaned_data['ssn_four_digit']:
            errors.append(forms.ValidationError("Enter last 4 digits of your Social Security Number"))

        if not self.cleaned_data['no_ssn'] and not self.cleaned_data['ssn_four_digit'].isnumeric():
            errors.append(forms.ValidationError("SSN digits must be numeric"))

        if self.cleaned_data['no_ssn'] and self.cleaned_data['ssn_four_digit']:
            errors.append(forms.ValidationError("Uncheck the 'I don't have SSN#' box OR "
                                                "erase the value in the Last 4 digits of SSN# box. Both can't be true"))

        if signature == '':
            errors.append(forms.ValidationError("Signature cannot be blank"))

        if tdate == '':
            errors.append(forms.ValidationError("Enter valid date"))

        if errors:
            raise forms.ValidationError(errors)
        else:
            return cleaned_data
