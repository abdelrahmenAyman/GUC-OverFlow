from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from ..serializers import GucianRetrieveSerializer, GucianUpdateSerializer
from ..models import Gucian
from ..permissions import IsProfileOwner


class GucianViewSet(GenericViewSet,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin):
    """
    Performs GET and PUT actions on Gucian instnaces.

    Author: Abdelrahmen Ayman
    """
    queryset = Gucian.objects.all()
    permission_classes = (IsProfileOwner,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GucianRetrieveSerializer
        elif self.action == 'update' or \
                self.action == 'partial_update':
            return GucianUpdateSerializer
