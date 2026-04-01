from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    qualification = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name

# Create your models here.
