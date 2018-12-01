from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from ..serializers import ResetPasswordSerializer
from ..models import Gucian


class ResetPasswordView(UpdateAPIView):
    """
    Sets password for the user corresponding to the given email.

    Author: Abdelrahmen Ayman
    """
    serializer_class = ResetPasswordSerializer
    queryset = Gucian.objects.all()

    def put(self, request, *args, **kwargs):
        user = Gucian.objects.get(pk=kwargs.get('pk')).user
        serializer = self.get_serializer(data=request.data, instance=user)

        # Validate and update user password if data is valid.
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response()
