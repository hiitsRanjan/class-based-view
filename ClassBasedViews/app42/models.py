from django.db import models

class EmployeeModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_no = models.IntegerField(unique=True)
    salary = models.FloatField()
    photo = models.ImageField(upload_to='employee_image')
    address = models.TextField()
    email_id = models.CharField(max_length=60,unique=True)
    password = models.CharField(max_length=60)