from django.db import models

class user(models.Model):
    name=models.CharField(max_length=60)
    family=models.CharField(max_length=60)
    email=models.EmailField()
    phone=models.BigIntegerField()


# Create your models here.
