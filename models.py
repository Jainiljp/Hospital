from django.db import models

class patientmodel(models.Model):
    Name =models.CharField(max_length=20)
    diagnosis =models.TextField(max_length=100)

# Create your models here.
