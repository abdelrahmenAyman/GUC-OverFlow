from django.db import models

from ..models import Course
from users.models import Gucian


class Question(models.Model):
    """
    Represents a question that can be asked on a specific course or topic.
    """
    course = models.ForeignKey(
        Course,
        related_name='questions',
        null=True,
        on_delete=models.SET_NULL)
    asker = models.ForeignKey(
        Gucian,
        related_name='questions',
        null=True,
        on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=30000)
    up_votes = models.IntegerField(default=1)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def votes(self):
        return self.up_votes - self.down_votes

    def up_vote(self):
        self.up_votes += 1
        self.save()

    def down_vote(self):
        self.down_votes += 1
        self.save()
