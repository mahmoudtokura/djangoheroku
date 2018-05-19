from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to="clients", blank=True, null=True)
    d_o_b = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

