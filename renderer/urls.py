from django.urls import path
from .views import render_timeline, render_login_email, render_password_login, render_profile

urlpatterns = [
    path('', render_timeline, name='timeline'),
    path('timeline/', render_timeline, name='timeline'),
    path('login/email/', render_login_email, name='login_email'),
    path('login/password/', render_password_login, name='login_password'),
    path('profile/', render_profile, name='profile'),]