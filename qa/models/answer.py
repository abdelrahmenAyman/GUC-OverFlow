from django.db import models

from ..models import Question
from users.models import Gucian


class Answer(models.Model):
    """
    Represents an answer to a question that was previously asked.
    """
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)
    answerer = models.ForeignKey(
        Gucian,
        related_name='answers',
        null=True,
        on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=30000)
    up_votes = models.IntegerField(default=1)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.up_votes - self.down_votes

    def up_vote(self):
        self.up_votes += 1
        self.save()

    def down_vote(self):
        self.down_votes += 1
        self.save()
