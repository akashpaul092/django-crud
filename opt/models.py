from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    addedDate = models.DateField(null=True)
    
    # python manage.py makemigration
    # pyton manage.py migrate