from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from ..serializers import QuestionSerializer, ListQuestionSerializer
from ..models import Question
from ..permissions import IsQuestionAsker

from users.models import Gucian


class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsQuestionAsker)

    def get_serializer_class(self):
        if self.action == 'list':
            return ListQuestionSerializer
        else:
            return QuestionSerializer

    def perform_create(self, serializer):
        """
        Sets the question asker to be the current authenticated user.
        """
        question_asker = Gucian.objects.get(user=self.request.user)
        serializer.save(asker=question_asker)

    @action(methods=['GET'], detail=True, url_path='up-vote')
    def up_vote(self, request, pk=None):
        """performs an up vote on the specified question."""
        question = get_object_or_404(klass=Question, pk=pk)
        question.up_vote()
        return Response('Up vote successfull')

    @action(methods=['GET'], detail=True, url_path='down-vote')
    def down_vote(self, request, pk=None):
        """performs an down vote on the specified question."""
        question = get_object_or_404(klass=Question, pk=pk)
        question.down_vote()
        return Response('Down vote successfull')
