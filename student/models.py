from django.db import models
from django.contrib.auth.models import User
from teacher.models import Teacher

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    full_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=50, default='B.tech')
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.full_name
    
 





