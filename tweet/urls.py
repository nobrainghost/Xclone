from django.urls import path
from .views import create_tweet,like_tweet,comment_tweet
from .views import time_line,users_tweets

urlpatterns = [
    path('create/', create_tweet, name='create_tweet'),
    path('like/', like_tweet, name='like_tweet'),
    path('comment/', comment_tweet, name='comment_tweet'),
    path('timeline/',time_line,name="timeline"),
    path('tweets/<str:username>',users_tweets,name='get_a_user_tweets'),
    path('action/<int:tweet_id>/like',like_tweet,name='like_tweet'),


]