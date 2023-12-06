from django.contrib import admin
from django.urls import path,include
from personality.views import person

urlpatterns = [
    path('', person)
]
