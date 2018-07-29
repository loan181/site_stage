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
    conceptExercises = conceptInfo.conceptexercise_set.all()

    print(conceptExercises)

    context = {
        'concept' : conceptInfo,
        'conceptExamples' : conceptExamples,
        'conceptExercises' : conceptExercises,
    }
    return render(request, 'concept.html', context)


def test(request):
    context = {
        'testStringPicture' : "Salut j'ai une imace juste ici  [img]blocs_orientations.PNG[/img] qui est dans static",
        'testStringSpoiler' : "Spoiler : [spoil=titre] Secret secret [img]blocs_orientations.PNG[/img] [/spoil] dingue",
        'testEmbedScratchProject' : "¨Projet Scratch : [/scratchProject=237288850] cool huh ?"
    }
    return render(request, 'test.html', context)
