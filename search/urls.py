from django.conf.urls import url , include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^search/',views.search,name='search'),
    url(r'^autosuggest/$',views.autosuggest, name='suggest'),
]