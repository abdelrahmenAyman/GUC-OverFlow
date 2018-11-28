from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from ..serializers import ForgetPasswordSerializer
from ..models import Gucian


class ForgetPasswordView(CreateAPIView):
    """
    Sends email with a link to reset password.

    Author: Abdelrahmen Ayman
    """
    serializer_class = ForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            gucian = Gucian.objects.get(guc_email=request.data.get('email'))
            domain = self.request.META.get('HTTP_HOST', '')
            gucian.send_forget_password_mail(domain=domain)
        except Gucian.DoesNotExist:
            pass

        return Response('Email sent if your mail exists')
