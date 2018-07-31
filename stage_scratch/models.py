from django.db import models


class Concept(models.Model):
    conceptName = models.CharField(max_length=100)
    conceptPreBlocksDescription = models.TextField(default="")
    # conceptBlocks = models.ImageField()
    conceptPostBlocksDescription = models.TextField(default="")

    def __str__(self):
        return self.conceptName


class ConceptExample(models.Model):
    exampleName = models.CharField(max_length=100)
    exampleConcept = models.ForeignKey(Concept, null=True, on_delete=models.SET_NULL)
    exampleNumber = models.IntegerField(default=0)
    exampleBlocks = models.TextField(null=True)
    exampleText = models.TextField()
    exampleOnlineProjectId = models.IntegerField(null=True)

    def __str__(self):
        return "Exemple " + str(self.exampleNumber) + " de " + str(self.exampleConcept) + " : " + self.exampleName


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


class ScratchBlock(models.Model):
    blockJson = models.CharField(max_length=200) # Voir : https://github.com/scratchblocks/scratchblocks/blob/master/locales/fr.json
    blockDescription = models.TextField()
    relatedConcept = models.ForeignKey(Concept, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Bloc : " +str(self.blockJson)