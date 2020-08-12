from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home
app_name = 'prac'
urlpatterns = [
    path('',home.as_view(),name="home"),
]
