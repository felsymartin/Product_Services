from atexit import register
from django.urls import path
from . import views

urlpatterns=[
    path('login1',views.login,name='login'),
    path('register',views.register,name='register'),    
    path('logout/',views.logout,name='logout'),
    path('valid',views.register_valid, name = 'validemail')
    
]
