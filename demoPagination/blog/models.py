from django.db import models

# Create your models here.
class postModel(models.Model):
    title = models.CharField(max_length = 25)
    image = models.ImageField()
    body = models.TextField()
    
    def __str__(self):
        return self.title