from django.db import models

class User(models.Model):
    """User table"""
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, null=True)

class Data(models.Model):
    """Data table"""
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    spending = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    location = models.CharField(blank=True, null=True, max_length=30)
