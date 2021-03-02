from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    """ Custom User Model """

    SECRET_LENGTH = 15

    # null avoids crashing for existing objects to have null value
    # blank avoids mandatory inputs for forms

    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_key = models.CharField(max_length=SECRET_LENGTH, default="", blank=True)

    clear = models.BooleanField(default=False)
