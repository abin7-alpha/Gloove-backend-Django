from unicodedata import name
from django.urls import path

from auth_user.api.views.registration_views import registration_view, verify_email
from auth_user.api.views.login_view import login_view
from auth_user.api.views.valid_email_view import is_valid_email

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', login_view, name='login'),
    path('email_verify', verify_email, name='email_verify'),
    path('valid_email', is_valid_email, name='is_valid_email')
]
