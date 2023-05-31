from django.urls import path
from .views import UserRegistrationView, EditProfileForm
from django.contrib.auth import views as auth_views



urlpatterns = [
    
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', EditProfileForm.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view()),

    
    
    
]