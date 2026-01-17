from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', contact, name='contact'),
    path('success/', contact, name='contact_success'),
]