import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

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

    def send_forget_password_mail(self, domain):
        """
        Sends a mail including url that contains a link to reset password.

        Author: Abdelrahmen Ayman
        """
        message = f'{domain}/reset-password/?token={self.pk}'
        subject = 'Shipper Forgot Password'
        receivers = [self.user.email]

        send_mail(
            subject=subject,
            message=message,
            recipient_list=receivers,
            from_email=settings.EMAIL_HOST_USER
        )
