from django.db import models


class ConceptDescriptions(models.Model):
    conceptDescription = models.TextField()
    conceptBlocks = models.ImageField()


class Concept(models.Model):
    conceptName = models.CharField(max_length=100)
    conceptDescription = models.OneToOneField(ConceptDescriptions, null=True, on_delete=models.SET_NULL)


class ConceptExample(models.Model):
    exampleName = models.CharField(max_length=100)
    exampleConcept = models.ForeignKey(Concept, null=True, on_delete=models.SET_NULL)
    exampleText = models.TextField()


