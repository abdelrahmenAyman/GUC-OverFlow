from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions

from .serializers import PollSerializer
from .models import Poll
from users.models import Gucian


class PollsView(viewsets.GenericViewSet,
                mixins.CreateModelMixin):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        gucian = Gucian.objects.get(user=self.request.user)
        serializer.save(gucian=gucian)
