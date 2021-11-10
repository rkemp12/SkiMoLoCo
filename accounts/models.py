from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
	zipcode = models.PositiveIntegerField(null=True, blank=True)

"""class Mountain(models.Model):
	mountain = models.CharField(max_length=50) #add a max_length variable
	mt_location = models.PositiveIntegerField(null=True, blank=True)#need to figure out how Google API sends location variable
	winter_season = models.DateField() #need to figure out relationship with mountain
	summer_season = models.DateField()
"""