from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField("用户名", max_length=20, unique=True, default='')
    age = models.IntegerField('年龄', default=1)
