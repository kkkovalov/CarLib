from django.db import models

# Create your models here.

class Manufacturers(models.Model):
    manufactureId = models.AutoField(primary_key=True)
    manufactureName = models.CharField(max_length=100)
    manufactureYearFounded = models.DateField()
    manufactureHeadquarters = models.CharField(max_length=200)

class Models(models.Model):
    modelId = models.AutoField(primary_key=True)
    manufactureName = models.CharField(max_length=150)
    modelName = models.CharField(max_length=200)
    
