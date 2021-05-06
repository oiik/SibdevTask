from django.db import models

# Create your models here.
class Deals(models.Model):
  customer = models.CharField(max_length=50)
  item = models.CharField(max_length=50)
  total = models.IntegerField()
  quantity = models.IntegerField()
  date = models.DateTimeField()
  def __str__(self):
    return self.title

class File(models.Model):
  deals = models.FileField(blank=False, null=False)

class Test(models.Model):
  customer = models.CharField(max_length=50)
  #total__sum = models.IntegerField()
  def __str__(self):
    return self.title
