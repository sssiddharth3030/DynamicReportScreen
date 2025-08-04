from django.db import models

class Item(models.Model):
  vairantName = models.CharField(max_length=64)
  description = models.TextField()
  def __str__(self):
    return self.name