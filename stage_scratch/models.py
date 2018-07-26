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
    exampleText = models.TextField()

    def __str__(self):
        return self.exampleName + ' (' + str(self.exampleConcept) + ')'


