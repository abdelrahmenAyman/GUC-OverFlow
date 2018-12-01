from rest_framework import viewsets
from rest_framework import mixins

from users.models import Gucian

from ..serializers import AnswerSerializer
from ..models import Answer
from ..permissions import IsAnswerAnswerer


class AnswerViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
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
