from django.urls import re_path

from API import views

urlpatterns = [
    re_path(r'^movies/([0-9]+)$', views.movieApi),
    re_path(r'^movieFilter/?$', views.movieFilterApi),
    re_path(r'^actors/([0-9]+)$', views.deleteActorApi),
]