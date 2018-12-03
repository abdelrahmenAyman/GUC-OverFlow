from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from users.models import Gucian

from ..serializers import AnswerSerializer
from ..models import Answer
from ..permissions import IsAnswerAnswerer


class AnswerViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin):
    """
    Responsible for performing actions on Answer model objects.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAnswerAnswerer,)

    def perform_create(self, serializer):
        answerer = Gucian.objects.get(user=self.request.user)
        serializer.save(answerer=answerer)

    @action(methods=['GET'], detail=True, url_path='up-vote')
    def up_vote(self, request, pk=None):
        """performs an up vote on the specified answer."""
        answer = get_object_or_404(klass=Answer, pk=pk)
        answer.up_vote()
<<<<<<< HEAD
        answer.answerer.increase_reputation(amount=5)
=======
>>>>>>> b8aa6efe9b98ec938aa49e5e6a0a2594daac5b20

        return Response('Up Vote Successful')

    @action(methods=['GET'], detail=True, url_path='down-vote')
    def down_vote(self, request, pk=None):
        """performs a down vote on the specified answer."""
        answer = get_object_or_404(klass=Answer, pk=pk)
<<<<<<< HEAD
        answer.answerer.decrease_reputation(amount=1)
        answer.down_vote()

        down_voter = Gucian.objects.get(user=request.user)
        down_voter.decrease_reputation(amount=1)

=======
        answer.down_vote()

>>>>>>> b8aa6efe9b98ec938aa49e5e6a0a2594daac5b20
        return Response('Down Vote Successful')
