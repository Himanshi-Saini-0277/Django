from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key = True)
    emp_name = models.CharField(max_length =  50)
    emb_dob = models.DateTimeField()
    emp_address = models.CharField(max_length = 200)

class Book(models.Model):
    book_id = models.AutoField(primary_key = True)
    book_name = models.CharField(max_length =  50)

    class Meta:
        db_table = "MyBooks"
        