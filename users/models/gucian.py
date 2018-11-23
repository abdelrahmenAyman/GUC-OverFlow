import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Gucian(models.Model):
    """
    Represents a user profile.

    Author: Abdelrahmen Ayman
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    guc_email = models.EmailField()
    backup_email = models.EmailField()
    major = models.CharField(max_length=50)
    dash_number = models.IntegerField(default=0)
    birthdate = models.DateField()
    bio = models.CharField(max_length=350)
    reputation = models.IntegerField(default=1)
    joined_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def age(self):
        today = datetime.datetime.now()
        return today.year - self.birthdate.year
