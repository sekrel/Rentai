from django.template.defaulttags import url
from django.urls import path

from companysite import views

urlpatterns = [
    path('', views.NewsListView.as_view()),
]
