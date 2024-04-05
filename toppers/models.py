from django.db import models
from django.conf import settings
class TopperwithLabels(models.Model):
    image=models.ImageField(upload_to='imagesT',blank=True,null=True)
    
    label=models.CharField(max_length=250,blank=True,null=True)
    title=models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return self.label if self.label else self.title
# Create your models here.
