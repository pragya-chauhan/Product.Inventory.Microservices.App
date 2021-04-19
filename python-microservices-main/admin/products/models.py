from django.db import models

#properties used added to product---table in sql
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)

#user table
class User(models.Model):
    pass
