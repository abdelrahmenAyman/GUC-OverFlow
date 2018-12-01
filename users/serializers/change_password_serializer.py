from rest_framework import serializers

from ..serializers import PasswordBasedSerializer


class ChangePasswordSerializer(PasswordBasedSerializer):
    """
    Responsible for validating change password data.

    Author: Abdelrahmen Ayman
    """
    old_password = serializers.CharField(style={'input_type': 'password'})

    def update(self, instance, validated_data):
        """Set user password"""
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance

    def validate_old_password(self, value):
        """Checks wether old password is the correct password."""
        if not self.instance.check_password(value):
            raise serializers.ValidationError('Wrong Old Password')
        return value
