from django.db import models


class ConceptDescriptions(models.Model):
    conceptDescription = models.TextField()
    conceptBlocks = models.ImageField()


class Concept(models.Model):
    conceptName = models.CharField(max_length=100)
    conceptDescription = models.OneToOneField(ConceptDescriptions, on_delete=models.SET_NULL, primary_key=True)


class ConceptExample(models.Model):
    exampleName = models.CharField(max_length=100)
    exampleConcept = models.ForeignKey(Concept, on_delete=models.SET_NULL)
    exampleText = models.TextField()


