from django.urls import path
from .views import *
urlpatterns=[
    path('List',List,name='Hotels_List'),
    path('Add',Add,name='Hotel_Add'),
]