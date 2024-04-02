from django.db import models

class Todoapp(models.Model):


     
     task = models.CharField(max_length=255)