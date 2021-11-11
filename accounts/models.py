from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])