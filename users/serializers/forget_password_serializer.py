from rest_framework import serializers


class ForgetPasswordSerializer(serializers.Serializer):
    """
    Responsible for data validation of forget password view.

    Author: Abdelrahmen Ayman
    """
    email = serializers.EmailField()
