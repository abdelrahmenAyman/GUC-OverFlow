from rest_framework import serializers

from ..models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Validation for Question model"""

    answers = serializers.StringRelatedField()

    class Meta:
        model = Question
        fields = ('pk', 'created_at', 'course', 'asker',
                  'title', 'text', 'votes', 'answers')
        read_only_fields = ('asker', 'created_at')


class ListQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('created_at', 'course', 'asker', 'title', 'text', 'votes')
