from django.db import models

class MountainDates(models.Model):
    mountain = models.CharField(max_length=200)
    winter_season_open = models.CharField(max_length=50, default="N/A")
    winter_season_close = models.CharField(max_length=50, default="N/A")
    summer_season_open = models.CharField(max_length=50, default="N/A")
    summer_season_close = models.CharField(max_length=50, default="N/A")
    link = models.CharField(max_length=2083, default="")
