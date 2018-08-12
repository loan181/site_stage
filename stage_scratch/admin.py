from django.contrib import admin

from .models import *


class ConceptAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'conceptName', 'conceptNumber')
    search_fields = ('conceptName',)


class ConceptExampleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'exampleName', 'exampleConcept', 'exampleNumber', 'exampleText')
    search_fields = ('exampleName', 'exampleText')


class ConceptExerciseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'exerciseName', 'exerciseConcept', 'exerciseNumber', 'exerciseStatement')
    search_fields = ('exerciseName', 'exerciseStatement')


class ConceptExerciseHintAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'hintExercise', 'hintNumber', 'hintContent')
    list_filter = ('hintExercise__exerciseConcept', 'hintExercise__exerciseNumber')
    search_fields = ('hintContent',)


class ScratchBlockAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'blockJson', 'blockDescription', 'relatedConcept',)
    list_filter = ('additionalBlocks',)
    search_fields = ('blockJson', 'blockDescription')


toRegister = {
    Concept : ConceptAdmin,
    ConceptExample : ConceptExampleAdmin,
    ConceptExercise : ConceptExerciseAdmin,
    ConceptExerciseHint : ConceptExerciseHintAdmin,
    ScratchBlock : ScratchBlockAdmin,
}
for toReg, toRegAdmin in toRegister.items() :
    print(toReg, toRegAdmin)
    admin.site.register(toReg, toRegAdmin)



