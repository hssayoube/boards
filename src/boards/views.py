from django.shortcuts import render
from .models import Board
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView

# Create your views here.
class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'index.html'