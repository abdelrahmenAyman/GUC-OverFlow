from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    """
    Responsible for validating change password data.

    Author: Abdelrahmen Ayman
    """
    old_password = serializers.CharField(style={'input_type': 'password'})
    new_password = serializers.CharField(style={'input_type': 'password'})
    confirm_password = serializers.CharField(style={'input_type': 'password'})

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

    def validate(self, attrs):
        if not self._are_passwords_matching(attrs):
            raise serializers.ValidationError('Passwords are not matching')
        return attrs

    def _are_passwords_matching(self, attrs):
        """
        Checks wether the new password and its confirmation are matching.

        Author: Abdelrahmen Ayman
        """
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')

        if new_password != confirm_password:
            return False
        return True
