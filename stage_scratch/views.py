from django.shortcuts import render

from .models import *

def index(request):
    context = {
        'concepts' : Concept.objects.all()
    }
    return render(request, 'index.html', context)

# Create your views here.
