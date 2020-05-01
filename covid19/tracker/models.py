from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Tracker(models.Model):
    totaltest = models.IntegerField(default = 0)
    totalpositive = models.IntegerField(default = 0)
    totalcollection = models.IntegerField(default = 0)
    date = models.CharField(default = "_", max_length = 20)


    def __str__ (self):
        return self.date
