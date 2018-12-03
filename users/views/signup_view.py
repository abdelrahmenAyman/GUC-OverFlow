from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from ..serializers import SignUpSerializer


class SignUpView(CreateAPIView):
    """
    Creates a new Gucian instance associated with a user instance.

    Author: Abdelrahmen Ayman
    """
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data={'detail': 'You signed up successfully'})
