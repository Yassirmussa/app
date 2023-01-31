from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField( upload_to='images/', default = None, height_field=None, width_field=None, max_length=None)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=False)
    db_table ='food_food'
class Product(models.Model):
    nam = models.CharField(max_length=200)
    img = models.FileField(upload_to="pictures")
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    
class Marina_officer(models.Model):
    Oname = models.CharField(max_length=200)
    Oaddress = models.CharField(max_length=200)
    Mname = models.CharField(max_length=200)
    Ophone = models.IntegerField()
    password = models.CharField(max_length=200)
    confpass = models.CharField(max_length=200, default="yassir 23")
    email = models.EmailField()

class Fishermen(models.Model):
    Fname = models.CharField(max_length=200)
    Vname = models.CharField(max_length=200)
    Fphone = models.IntegerField()
    Faddress = models.CharField(max_length=200)