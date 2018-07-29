from django.db import models


class ConceptDescriptions(models.Model):
    conceptDescription = models.TextField()
    conceptBlocks = models.ImageField()

    def __str__(self):
        return self.conceptDescription


class Concept(models.Model):
    conceptName = models.CharField(max_length=100)
    conceptDescription = models.OneToOneField(ConceptDescriptions, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.conceptName


class ConceptExample(models.Model):
    exampleName = models.CharField(max_length=100)
    exampleConcept = models.ForeignKey(Concept, null=True, on_delete=models.SET_NULL)
    exampleBlocks = models.TextField(null=True)
    exampleText = models.TextField()
    exampleOnlineProjectId = models.IntegerField(null=True)

    def __str__(self):
        return self.exampleName + ' (' + str(self.exampleConcept) + ')'


class ConceptExercise(models.Model):
    exerciseName = models.CharField(max_length=100)
    exerciseConcept = models.ForeignKey(Concept, null=True, on_delete=models.SET_NULL)
    exerciseNumber = models.IntegerField()
    exerciseStatement = models.TextField()

    def __str__(self):
        return "Ex "+str(self.exerciseNumber)+" : "+self.exerciseName + ' (' + str(self.exerciseConcept) + ')'


class ConceptExerciseHint(models.Model):
    hintExercise = models.ForeignKey(ConceptExercise, null=True, on_delete=models.SET_NULL)
    hintNumber = models.IntegerField()
    hintContent = models.TextField()

    def __str__(self):
        return "indice " + str(self.hintNumber) + " de " + str(self.hintExercise)

