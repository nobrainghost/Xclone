from django.urls import path
from .views import create_tweet,like_tweet,comment_tweet

urlpatterns = [
    path('create/', create_tweet, name='create_tweet'),
    path('like/', like_tweet, name='like_tweet'),
    path('comment/', comment_tweet, name='comment_tweet'),

]