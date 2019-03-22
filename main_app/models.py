from django.db import models

class Wish(models.Model):
    description=models.TextField(max_length=250)



# Create your models here.
