from django.db import models

class Proyecto(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()
    tecnology= models.CharField(max_length=200)
    created_at= models.DateTimeField(auto_now_add=True)
