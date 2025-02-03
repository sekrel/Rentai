from django.template.defaulttags import url
from django.urls import path

from companysite import views

urlpatterns = [
    path('new', views.NewsListView.as_view()),
    path('games', views.GamesListView.as_view()),
    path('about', views.about),
]
