from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import New, Game, Creation
from .forms import ProductForm



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
    
class CreationListView(ListView):
    model = Creation
    template_name = 'companysite/creations.html'
    context_object_name = 'posts'
    extra_context={
        'title': 'Фанатское творчество', 
    }
    

class AddCreationCreateView(CreateView):
    form_class = ProductForm 
    template_name = 'companysite/add_creation.html'
    success_url = reverse_lazy('creation')
    extra_context={
        'title': 'Фанатское творчество',
    }
   