from django.urls import path
from .views import get_user_profile,update_user_profile,delete_user_profile


urlpatterns = [
    path('profile/', get_user_profile, name='profile'),
    path('profile/update/', update_user_profile, name='update_profile'),
    path('profile/delete/', delete_user_profile, name='delete_profile'),]
