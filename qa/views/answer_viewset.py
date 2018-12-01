from rest_framework import viewsets
from rest_framework import mixins

from users.models import Gucian

from ..serializers import AnswerSerializer


class AnswerViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin):
    """
    Responsible for performing actions on Answer model objects.
    """
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        answerer = Gucian.objects.get(user=self.request.user)
        serializer.save(answerer=answerer)
