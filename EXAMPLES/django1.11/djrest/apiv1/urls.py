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
    url(r'^herolist$', views.superhero_list, name='superherolist'),
    url(r'^hero/(?P<pk>\d+)', views.superhero_detail, name='superherodetail'),
    url(r'^enemylist', views.EnemyList.as_view(), name='enemylist'),
    url(r'^enemy/(?P<pk>\d+)', views.EnemyDetail.as_view(), name='enemydetail'),
]
