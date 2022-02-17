from django.urls import path
from . import views

urlpatterns=[
    #path('',views.productdetails,name='productdetails'),
    path('<int:pageid>/',views.productdetails_2,name='productdetails'),
    path('comment/',views.commenttext,name='commenttext')
      
]
