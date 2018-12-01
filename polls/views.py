from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from ..serializers import PollsSerializer


class PollsView(CreateAPIView):
    serializer_class = PollsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data={'detail': 'You created poll successfully'})

# Create your views here.
