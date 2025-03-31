from django.urls import path
from companysite import views


urlpatterns = [
    path('', views.about, name = 'home'),
    path('new/', views.NewsListView.as_view(), name = 'new'),
    path('games/', views.GamesListView.as_view(), name = 'games'),
    path('creation/', views.CreationListView.as_view(), name = 'creation'),
    path('add_creation/', views.AddCreationCreateView.as_view(), name = 'add_creation'),
]
