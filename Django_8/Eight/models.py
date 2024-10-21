from django.db import models

# Create your models here.
class PlantsDetail(models.Model):  
    pid = models.IntegerField(primary_key=True)  
    plant_name = models.CharField(max_length=100)  
 