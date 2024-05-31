from django.db import models


class Company(models.Model):
  name = models.CharField(max_length=200)
  bio = models.TextField(max_length=300,blank=True, null=True)

  def __str__(self):
    return self.name



class Advocate(models.Model):
  company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
  username = models.CharField(max_length=200)
  bio = models.TextField(max_length=300,blank=True, null=True)

  def __str__(self):
    return self.username