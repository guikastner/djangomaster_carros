from django.db import models

# Create your models here.

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True,null=True)
    model_year = models.IntegerField(blank=True,null=True)
    value = models.FloatField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): # Generate a string representation of the model
        return self.model