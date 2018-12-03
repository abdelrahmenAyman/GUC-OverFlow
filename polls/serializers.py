# from rest_framework import serializers
# from polls.models import Poll


# class PollsSerializer(serializers.Serializer):
#     question = serializers.CharField(
#         required=True, allow_blank=False, max_length=200)
#     pub_date = serializers.DateTimeField('date published')
#     user = serializers.get_user_model()

#     def create(self, validated_data):
#         return Poll.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.question = validated_data.get('question', instance.question)
#         instance.pub_date = validated_data.get('pub_date', instance.pub_date)
#         instance.user = validated_data.get('user', instance.user)
#         instance.save()
#         return instance
from rest_framework import serializers
from .models import Poll, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ('question', 'pub_date', 'gucian', 'choices')
        read_only_fields = ('gucian',)
