from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class Portfolio(ListView):
    template_name = 'portfolio/portfolio.html'
    model = Project
    context_object_name = 'projects'
