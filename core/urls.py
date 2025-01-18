from django.urls import path
from .views import register_user, protected,logout

urlpatterns = [
    path('register/', register_user, name='register'),
    path('protected/', protected, name='protected'),
    path('logout/', logout, name='logout'),
    
]