from django.contrib import admin

from .models import *

toRegister = (Concept, ConceptExample, ConceptExercise, ConceptExerciseHint, ScratchBlock)

for toReg in toRegister :
    admin.site.register(toReg)
