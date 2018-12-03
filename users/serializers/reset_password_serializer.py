from ..serializers import PasswordBasedSerializer


class ResetPasswordSerializer(PasswordBasedSerializer):
    """
    Validates data for reset password view.

    Author: Abdelrahmen Ayman
    """

    def update(self, instance, validated_data):
        """Set user password"""
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
