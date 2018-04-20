"""
URL Configuration for bands
"""
from django.conf.urls import url
from . import views   # import views from app
from . import classviews

urlpatterns = [
    # add url patterns for the bands app here

    # Example:
    url(r'^$', views.home, name='home'),
    url(r'^sorted$', views.bands_sorted, name='bandssorted'),
    url(r'^list$', views.bands_list, name='bandslist'),
    url(r'^classlist$', classviews.BandListView.as_view(), name='bandsclasslist'),
    url(r'^class/(?P<pk>\d+)$', classviews.BandDetailView.as_view(), name='bandclassdetails'),
    url(r'^listmore$', views.bands_list_more, name='bandslistmore'),
    url(r'^genre/(?P<genre_name>[\w\s]+)$', views.bands_by_genre, name='bandsbygenre'),
    url(r'^search/(?P<search_term>[\w\s]+)$', views.bands_search, name='bandssearch'),
    url(r'^(?P<id>\d+)$', views.band_details, name='banddetails'),
    url(r'^(?P<band_name>[\w\s]+)$', views.band_basic, name='bandbasic'),
]
