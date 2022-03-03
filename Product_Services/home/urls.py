from django.urls import path
from . import views
from .feed import LatestPostFeed

urlpatterns=[
    path('',views.home,name='home'),
    path('feed/', LatestPostFeed(), name='productupdationfeed'),
    path('complete/', views.search, name='inputautocomplete'),
    path('email', views.email, name='mailing')
]