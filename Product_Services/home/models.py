from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    charge = models.IntegerField()
    image = models.ImageField(upload_to = 'pics')
    date = models.DateTimeField(auto_now_add = True)
    offer = models.BooleanField(default = False)
