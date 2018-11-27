from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..serializers import ChangePasswordSerializer


class ChangePasswordView(CreateAPIView):
    """
    Changes the requesting user password.

    Author: Abdelrahmen Ayman
    """

    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Password Changed Successfully')
