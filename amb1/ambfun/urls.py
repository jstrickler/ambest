"""
URL Configuration for ambfun
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the ambfun app here

    # Example:
#    url(r'^$', views.home, name='home'),
     url(r'^$', views.index, name='index'),
     url(r'toast', views.toast, name='toast'),
]
