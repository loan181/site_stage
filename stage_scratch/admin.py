from django.contrib import admin

from .models import *

admin.site.register(Concept)
admin.site.register(ConceptDescriptions)
admin.site.register(ConceptExample)
admin.site.register(ConceptExercise)
admin.site.register(ConceptExerciseHint)



# Register your models here.
