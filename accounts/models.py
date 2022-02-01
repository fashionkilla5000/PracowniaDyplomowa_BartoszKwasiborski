"""Account models."""
# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import SET_NULL

# from planner.models import Class


class CustomUser(AbstractUser):  # noqa: D101

    is_dostawca = models.BooleanField(default=False)
    is_kelner = models.BooleanField(default=False)

    def str(self):  # noqa: D105
        return f'{self.get_full_name()}'