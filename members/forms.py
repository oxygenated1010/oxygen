from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        
        
        # This is used to bootstrap the edit profile page
class EditMyProfileForm(UserChangeForm):  
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_active', 'date_joined')


        



