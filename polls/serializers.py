from rest_framework import serializers
from .models import Poll, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice', 'votes')
        read_only_fields = ('votes',)


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('question', 'pub_date', 'gucian', 'choices')
        read_only_fields = ('gucian', 'choices')


class VoteUpSerializer(serializers.Serializer):
    choice_pk = serializers.IntegerField()
