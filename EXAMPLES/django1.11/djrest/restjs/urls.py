"""
URL Configuration for restjs
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the restjs app here

    # Example:
   url(r'^home', views.home, name='home'),
]
