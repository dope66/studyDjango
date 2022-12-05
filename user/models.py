from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    mobile =models.CharField(max_length=12)
    gender =models.CharField(max_length=1,
                             choices=(
                                 ('f','female'),
                                 ('m','male')
                             ),default='m')

