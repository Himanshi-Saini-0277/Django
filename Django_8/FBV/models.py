from django.db import models

class Plants(models.Model):  
    pid = models.CharField(max_length=20)  
    plant_name = models.CharField(max_length=100)  
    plant_price = models.IntegerField()
    class Meta:  
        db_table = "plantdata"  
