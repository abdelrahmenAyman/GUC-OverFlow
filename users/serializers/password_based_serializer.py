from rest_framework import serializers


class PasswordBasedSerializer(serializers.Serializer):
    """
    Provides a set of common operations to be used by serializers that 
    validates passwords.

    Author: Abdelrahmen Ayman
    """
    new_password = serializers.CharField(style={'input_type': 'password'})
    confirm_password = serializers.CharField(style={'input_type': 'password'})

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
