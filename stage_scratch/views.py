from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.templatetags.static import static
from django.shortcuts import redirect


from .models import *


def index(request):
    context = {
        'allConceptName': getAllconceptsName(),
        'concepts' : Concept.objects.all(),
        'projects' : Project.objects.all(),
    }
    return render(request, 'index.html', context)


def getAllconceptsName():
    return tuple(Concept.objects.values_list('conceptName', flat=True))

def isLocalhost(request):
    host = request.get_host()
    return host.startswith('127.0.0.1') or host.startswith('localhost')

def concept(request, concept_name):
    conceptInfo = get_object_or_404(Concept, conceptName=concept_name)
    conceptBlocks = conceptInfo.scratchblock_set.all()
    conceptExamples = conceptInfo.conceptexample_set.all()
    conceptExercises = conceptInfo.conceptexercise_set.all()

    nextConcept = Concept.objects.filter(id__gt=conceptInfo.id).order_by('id')[:1].first()
    lastConcept = Concept.objects.filter(id__lt=conceptInfo.id).order_by('-id')[:1].first()
    nextConceptName = None
    if nextConcept != None:
        nextConceptName = nextConcept.conceptName
    lastConceptName = None
    if lastConcept != None:
        lastConceptName = lastConcept.conceptName

    localhost = isLocalhost(request)

    context = {
        'allConceptName' : getAllconceptsName(),
        'concept' : conceptInfo,
        'conceptBlocks' : conceptBlocks,
        'conceptExamples' : conceptExamples,
        'conceptExercises' : conceptExercises,
        'conceptNext' : nextConceptName,
        'conceptLast' : lastConceptName,
        'admin' : localhost,
    }
    return render(request, 'concept.html', context)


def myProject(request):
    context = {
        'allConceptName': getAllconceptsName(),
    }
    return render(request, 'projectCustom.html', context)


def project(request, project_name):
    project = get_object_or_404(Project, projectTitle=project_name)
    projectSprites = project.projectsprite_set.all()
    context = {
        'allConceptName': getAllconceptsName(),
        'project': project,
        'projectSprites': projectSprites,
        'admin': isLocalhost(request),
    }
    return render(request, 'project.html', context)

def slide(request):
    slides = Slide.objects.all() # TODO : mettre dans l'ordre croissant des numéros
    slideCategories = slides.select_related('slideCategory').values('slideCategory__categoryName').distinct()
    context = {
        'allConceptName': getAllconceptsName(),
        'allSlides': slides,
        'slideCategories': slideCategories,
    }
    return render(request, 'slide.html', context)


def scratchOffline(request):
    context = {
    }
    return render(request, 'scratch.html', context)


def locale(request, fileName):
    staticPath = static("scratch/locale/")+fileName # Nécessaire car pas facile de changer le code de Scratch
    return redirect(staticPath)


def test(request):
    context = {
        'testStringPicture' : "Salut j'ai une imace juste ici  [img]blocs_orientations.PNG[/img] qui est dans static",
        'testStringSpoiler' : "Spoiler : [spoil title=titre id=eza] Secret secret [img]blocs_orientations.PNG[/img] [/spoil] dingue",
        'testEmbedScratchProject' : "¨Projet Scratch : [/scratchProject=237288850] cool huh ?"
    }
    return render(request, 'test.html', context)