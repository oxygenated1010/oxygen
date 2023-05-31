from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditMyProfileForm

# Create your views here.

class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class EditProfileForm(generic.UpdateView): # Here we used the UpdateView class
    form_class = EditMyProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):      # This helps the edit profile page to get the correct data
        return self.request.user

