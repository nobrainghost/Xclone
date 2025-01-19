from django.urls import path
from .views import follow_a_user,unfollow_someone,fetch_following,fetch_followers

urlpatterns=[
    path('follow/<str:username>/',follow_a_user,name='follow'),
    path('unfollow/<str:username>/',unfollow_someone,name='unfollow'),
    path('followers/<str:username>/',fetch_followers,name='follwers'),
    path('following/<str:username>/',fetch_following,name='following'),
]