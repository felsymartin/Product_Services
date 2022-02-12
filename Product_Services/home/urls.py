from django.urls import path
from . import views
from .feed import LatestPostFeed

urlpatterns=[
    path('',views.home,name='home'),
    path('feed/', LatestPostFeed(), name='productupdationfeed')
]