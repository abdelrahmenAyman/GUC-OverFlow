from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializers import PollSerializer, VoteUpSerializer, ChoiceSerializer
from .models import Poll, Choice
from users.models import Gucian


class PollsView(viewsets.GenericViewSet,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.ListModelMixin):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        gucian = Gucian.objects.get(user=self.request.user)
        serializer.save(gucian=gucian)

    @action(methods=['POST'],
            detail=True, url_path='up-vote', serializer_class=VoteUpSerializer)
    def up_vote(self, request, pk=None):
        """performs an up vote on the specified choice."""
        choice_pk = request.data['choice_pk']
        choice = get_object_or_404(klass=Choice, pk=choice_pk, poll__pk=pk)
        choice.votes += 1
        choice.save()

        return Response('Up Vote Successful')

    @action(methods=['POST'],
            detail=True, url_path='add-choice',
            serializer_class=ChoiceSerializer)
    def add_choice(self, request, pk=None):
        poll = get_object_or_404(klass=Poll, pk=pk)
        choice_text = request.data['choice']
        new_choice = Choice(choice=choice_text, poll=poll)
        new_choice.save()

        return Response('Choice Added')
