import datetime
from django.db import models

from users.models import Gucian


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    gucian = models.ForeignKey(
        Gucian,
        null=True,
        on_delete=models.SET_NULL,
        related_name='polls'
    )

    def __unicode__(self):
        return self.question

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()


class Choice(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        verbose_name="the related poll",
        related_name='choices'
    )
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.question
