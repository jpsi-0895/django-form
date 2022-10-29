from django.db import models

# Create your models here.

class Register(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()
    
    def __str__(self):
        return self.fullname