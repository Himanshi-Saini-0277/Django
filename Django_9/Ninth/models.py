from django.db import models

class AppUsers(models.Model):  
    user_id = models.AutoField(primary_key=True)  
    user_name = models.CharField(max_length=100)  
    user_password = models.CharField(max_length=20)
    user_email = models.EmailField()
    class Meta:  
        db_table = "userData" 

