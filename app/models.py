from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length = 50)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length = 50)
    
    # def __str__(self):
    #     return self.email

class St(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_contact = models.IntegerField()
    stu_city = models.CharField(max_length=50)
    def __str__(self):
        return self.stu_name
