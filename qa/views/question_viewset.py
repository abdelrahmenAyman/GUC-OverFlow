from rest_framework import viewsets
from rest_framework import permissions

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
