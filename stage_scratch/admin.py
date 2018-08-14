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


class SlideAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slideTitle', 'slideNumber', 'slideRelatedConcept')
    search_fields = ('slideTitle', )

def adminRegister():
    namespace = globals()
    for name, model_admin in namespace.items():
        if name.endswith("Admin"):
            model = namespace[name[:-5]]
            try:
                admin.site.register(model, model_admin)
            except :
                print("Unexpected error in admin.py when trying to auto-generate admin database")
                raise


adminRegister()

