from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from eat.models import Application

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


class Step2Form(forms.Form):
    CHOICES = (
        ('yes', 'Yes',),
        ('no', 'No',)
    )
    assistanceProgram = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    caseNumber = forms.CharField(max_length=50, required=False)

    def clean_caseNumber(self):
        if self.cleaned_data['assistanceProgram'] == 'yes' and self.cleaned_data['caseNumber'] == '':
            raise forms.ValidationError('Case number is mandatory if you are currently participating in an assistance'
                                        ' program')
        else:
            return self.cleaned_data['caseNumber']


class StepForm(forms.Form):
    class Meta:
        model = Application
        fields = ['assistance_program', 'case_number']