from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import New, Game



class NewsListView(ListView):
    model = New
    template_name = 'companysite/news.html' 
    context_object_name = 'posts'
    
    extra_context={
        'title': 'Новости', 
    }

class GamesListView(ListView):
    model = Game
    template_name = 'companysite/games.html'
    context_object_name = 'posts'
    
    extra_context={
        'title': 'Наши игры', 
    }

# class AboutListView(ListView):
#     template_name = 'companysite/about.html'
#     context_object_name = 'posts'
    
#     extra_context={
#         'title': 'О нашей компании', 
#     }


def about(request):
    return render(request, 'companysite/about.html', {'title': 'О нашей компании'})
    
    
