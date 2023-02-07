from django.urls import path
from .views import *
urlpatterns=[
    path('Login2', Loginview.as_view(), name='Login2'),
    path('Logout2', mylogout2, name='Logout2'),
    path('Register2', myregister2, name='Register2'),
    path('List', List.as_view(), name='Account_List'),
]