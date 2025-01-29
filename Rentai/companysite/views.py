from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import New


class NewsListView(ListView):
    model = New
    template_name = 'companysite/base.html' 
    context_object_name = 'posts'
    
    extra_context={
        'title': 'Новости', 
    }
    
    
