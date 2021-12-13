from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SearchForm

def get_city(request):
    form = SearchForm(request.GET)
    return render(request, 'home/index.html', {'form':form})

def index(request):
    return render(request, 'home/index.html')