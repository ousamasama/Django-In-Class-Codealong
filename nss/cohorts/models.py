from django.db import models

# Create your models here.
class Cohort(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=120)
    fave_color = models.CharField(max_length=120)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)

    def __str__(self):
        return self.name