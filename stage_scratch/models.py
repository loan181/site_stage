from django.db import models


class Category(models.Model):
    categoryName = models.CharField(max_length=50, help_text="Texte/titre de la catégorie")

    def __str__(self):
        return "Categorie " + self.categoryName


class Concept(models.Model):
    conceptName = models.CharField(max_length=100, help_text="Titre du concept")
    conceptNumber = models.IntegerField(unique=True, blank=True, null=True, help_text="Numéro du concept (pas grave s'ils ne se suivent pas, ils servent pour donner un ordre logique)")
    conceptPreBlocksDescription = models.TextField(default="", help_text="Description courte avant que les blocs soit données")
    conceptPostBlocksDescription = models.TextField(default="", blank=True, null=True, help_text="Description après que les blocs soit données")

    def __str__(self):
        return self.conceptName


class ConceptExample(models.Model):
    exampleName = models.CharField(max_length=100, help_text="Titre de l'exemple")
    exampleConcept = models.ForeignKey(Concept, null=True, on_delete=models.SET_NULL, help_text="Concept auquel est attaché cet exemple")
    exampleNumber = models.IntegerField(default=0, help_text="Numéro de l'exemple (pas grave s'ils ne se suivent pas, ils servent pour donner un ordre logique)")
    exampleBlocks = models.TextField(null=True, help_text="Blocs utilisés pour la réalisation de l'exemple")
    exampleText = models.TextField(help_text="Description de l'exemple")
    exampleOnlineProjectId = models.IntegerField(null=True, help_text="ID utilisé sur le site de scratch pour une démo de l'exemple")

    def __str__(self):
        return "Exemple " + str(self.exampleNumber) + " de " + str(self.exampleConcept) + " : " + self.exampleName


class ConceptExercise(models.Model):
    exerciseName = models.CharField(max_length=100, help_text="Titre de l'exercice")
    exerciseConcept = models.ForeignKey(Concept, null=True, on_delete=models.SET_NULL, help_text="Concept auquel est lié cet exercice")
    exerciseNumber = models.IntegerField(help_text="Numéro de l'exercice (pas grave s'ils ne se suivent pas, ils servent pour donner un ordre logique)")
    exerciseStatement = models.TextField(help_text="enoncé de l'exercice")

    def __str__(self):
        return "Ex "+str(self.exerciseNumber)+ ' (' + str(self.exerciseConcept) + ')'+" : "+self.exerciseName


class ConceptExerciseHint(models.Model):
    hintExercise = models.ForeignKey(ConceptExercise, null=True, on_delete=models.SET_NULL, help_text="Exercice auquel cet indicé est lié")
    hintNumber = models.IntegerField(help_text="Numéro de l'indice (pas grave s'ils ne se suivent pas, ils servent pour donner un ordre logique)")
    hintContent = models.TextField(help_text="Contenu textuel de l'indice")

    def __str__(self):
        return "indice " + str(self.hintNumber) + " de " + str(self.hintExercise)


class Slide(models.Model):
    slideTitle = models.CharField(max_length=50, help_text="Titre des slides")
    slideLink = models.CharField(max_length=150, help_text="partie distincte de l'URL menant vers les slides en ligne")
    slideNumber = models.IntegerField(help_text="Numéro de la slide (pas grave s'ils ne se suivent pas, ils servent pour donner un ordre logique)")
    slideRelatedConcept = models.ForeignKey(Concept, null=True, blank=True, on_delete=models.SET_NULL, help_text="Concept pour le quel les slides s'applique")
    slideCategory = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, help_text="Catégorie de la slide")

    def __str__(self):
        return "Slide " + self.slideTitle


class Project(models.Model):
    projectTitle = models.CharField(max_length=50, help_text="Titre/Nom du projet")
    projectThumbnail = models.CharField(max_length=50, help_text="Nom de l'aperçu du projet dans static/img/projectsPreview")
    projectSummary = models.TextField(help_text="Court texte de description du project")
    projectOnlineProjectId = models.IntegerField(null=True, help_text="ID utilisé sur le site de scratch pour une démo du projet")
    projectGameGoal = models.TextField(help_text="Définir l'ensemble des règles du jeu")

    def __str__(self):
        return "Project " + self.projectTitle


class ProjectSprite(models.Model):
    projectSpriteName = models.CharField(max_length=50, help_text="Nom du lutin")
    projectSpriteRelatedProject = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, help_text="Projet auquel ce lutin est lié")

    def __str__(self):
        return "Sprite " + self.projectSpriteName + " (" + str(self.projectSpriteRelatedProject) + ")"


class ProjectSpriteObjective(models.Model):
    projectSpriteObjectiveTitle = models.CharField(max_length=50, help_text="Titre/Nom de l'objectif")
    projectSpriteObjectiveNumber = models.IntegerField(help_text="Numéro de l'objectif (pas grave s'ils ne se suivent pas, ils servent pour donner un ordre logique)")
    projectSpriteObjectiveRelatedProjectSprite = models.ForeignKey(ProjectSprite, null=True, on_delete=models.SET_NULL, help_text="Sprite du projet auquel cet objectif de lutin est lié")
    projectSpriteObjectiveExplanation = models.TextField(help_text="Détail sur l'objectif")

    def __str__(self):
        return "Sprite Objective " + self.projectSpriteObjectiveTitle + "("+str(self.projectSpriteObjectiveRelatedProjectSprite)+")"


class ScratchBlock(models.Model):
    blockJson = models.TextField(max_length=200, help_text="Voir : https://github.com/scratchblocks/scratchblocks/blob/master/locales/fr.json")
    blockDescription = models.TextField(help_text="Description du bloc")
    relatedConcept = models.ForeignKey(Concept, null=True, blank=True, on_delete=models.SET_NULL, help_text="Concept nécessitant l'utilisation de ce bloc")
    additionalBlocks = models.ManyToManyField(ConceptExercise, blank=True, help_text="Blocs additionnels d'un exercice n'ayant pas encore vu au stade du chapitre courant")
    helpBlocks = models.ManyToManyField(ProjectSpriteObjective, blank=True, help_text="Blocs pour aider à guider lors de la réalisation d'un projet")
    # scratchDocumentationLinkName = models.CharField(max_length=150, null=True, blank=True, help_text="Nom dans l'url tel que définit sur le wiki de scratch : https://fr.scratch-wiki.info/wiki/Cat%C3%A9gorie:Blocs")
    # déterminable en utilisant le Json du bloc

    def __str__(self):
        return "Bloc : " +str(self.blockJson)