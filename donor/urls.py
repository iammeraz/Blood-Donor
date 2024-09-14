# donor/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_donor, name='add_donor'),
    path('list/', views.donor_list, name='donor_list'),
    # Other URL patterns
]
