from django.db import models
from django.contrib.auth.models import User

class Ramen(models.Model):
    brand = models.CharField(max_length=100)
    flavour = models.CharField(max_length=100)
    spice = models.CharField(max_length=100)
<<<<<<< HEAD
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> bb530e78dc8c5916f244b192e72ae2aab440a23a

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

<<<<<<< HEAD

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
=======
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)    

    
>>>>>>> bb530e78dc8c5916f244b192e72ae2aab440a23a
