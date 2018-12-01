from rest_framework import serializers

from ..models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    """Responsible for validating data interacting with Answer model."""

    class Meta:
        model = Answer
        fields = ('pk', 'created_at', 'question', 'text', 'votes', 'answerer')
        read_only_fields = ('answerer',)
