from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.forms import EmailInput, TextInput, Select, PasswordInput
from django.contrib.auth import password_validation
from .models import CustomUser
from . import countries as c

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'name', 'organization', 'country')

        widgets = {'email':EmailInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Email'}),
                   'name':TextInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Name'}),
                   'organization':TextInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Organization'}),
                   'country':Select(attrs={'class':'form-control', 'required':True, 'placeholder':'Country'}, choices=c.getCountries()),
                #    'is_superuser':CheckboxInput(attrs={'class':'form-control inline-element', 'label':'Is Super User', 'required':False}),
                #    'is_active':CheckboxInput(attrs={'class':'form-control inline-element', 'label':'Is Active', 'required':False}),
                #    'is_staff':CheckboxInput(attrs={'class':'form-control inline-element', 'label':'Is Staff', 'required':False}),
                   'password1':PasswordInput(attrs={'class':'form-control', 'required':True, 'autocomplete':False, 'placeholder':'Password', 'help_text':password_validation.password_validators_help_text_html()}),
                   'password2':PasswordInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Password Confirmation'}),
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)