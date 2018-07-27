from django.shortcuts import get_object_or_404, render

from .models import *


def index(request):
    context = {
        'concepts' : Concept.objects.all()
    }
    return render(request, 'index.html', context)


def concept(request, concept_name):
    conceptInfo = get_object_or_404(Concept, conceptName=concept_name)
    conceptExamples = conceptInfo.conceptexample_set.all()

    context = {
        'concept' : conceptInfo,
        'conceptExamples' : conceptExamples
    }
    return render(request, 'concept.html', context)

# Create your views here.
def test(request):
    context = {'testString' : "Salut j'ai une imace juste ici  [img]blocs_orientations.PNG[/img] qui est dans static"}
    return render(request, 'test.html', context)