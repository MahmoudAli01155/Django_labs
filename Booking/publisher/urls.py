from django.urls import path
from .views import *
urlpatterns=[
    path('', ApiOverview, name='home'),
    path('create/', add_items, name='add-items'),
    path('all/', view_items, name='view_items'),
    path('update/<int:pk>/', update_items, name='update-items'),
    path('item/<int:pk>/delete/', delete_items, name='delete-items'),
]