"""
URL Configuration for apiv1
"""
from django.conf.urls import url
from . import views   # import views from app
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Superhero API')

urlpatterns = [
    # add url patterns for the apiv1 app here

    # Example:
    url(r'^$', schema_view, name='schema'),
    url(r'^heros/(?P<pk>\d+)', views.superhero_detail, name='superherodetail'),
    url(r'^heros$', views.superhero_list, name='herolist'),
    url(r'^enemylist', views.EnemyList.as_view(), name='enemylist'),
    url(r'^enemy/(?P<pk>\d+)', views.EnemyDetail.as_view(), name='enemydetail'),
    url(r'^powers/(?P<pk>\d+)', views.power, name="power"),
    url(r'^powers', views.power_list, name='powerlist'),
]
