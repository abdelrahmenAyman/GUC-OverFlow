import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Gucian

User = get_user_model()


class SignUpSerializer(serializers.Serializer):
    """
    Responsible for validating signup view input.

    Author: Abdelrahmen Ayman
    """
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    guc_email = serializers.EmailField()
    backup_email = serializers.EmailField()
    major = serializers.CharField()
    dash_number = serializers.IntegerField()
    birthdate = serializers.DateField()
    bio = serializers.CharField(required=False)
    password = serializers.CharField(style={'input_type': 'password'})
    confirm_password = serializers.CharField(style={'input_type': 'password'})

    def validate_guc_email(self, value):
        """ensures that it's a GUC email"""
        if not value.endswith('guc.edu.eg'):
            raise serializers.ValidationError('Please Enter a valid GUC email')
        return value

    def validate_birthdate(self, value):
        """Puts boundaries to user birthdate"""
        max_valid_year = datetime.datetime.now().year - 16

        if value.year < 1930:
            raise serializers.ValidationError('Invalid birthdate')

        if value.year > max_valid_year:
            raise serializers.ValidationError('Invalid birthdate')

        return value

    def validate_backup_email(self, value):
        """Ensures that backup email is not a GUC email too"""
        if value.endswith('guc.edu.eg'):
            raise serializers.ValidationError('Please enter a non GUC email')
        return value

    def create(self, validated_data):
        """Creates a new instance of Gucian"""
        user = self.create_user(validated_data)
        return self.create_gucian(validated_data, user)

    def create_user(self, validated_data):
        user_creation_data = {
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            'email': validated_data['guc_email'],
            'username': validated_data['guc_email'],
        }

        user = User.objects.create(**user_creation_data)
        user.set_password(validated_data['password'])
        return user

    def create_gucian(self, validated_data, user):
        gucian_creation_data = {
            'user': user,
            **validated_data
        }
        del gucian_creation_data['first_name']
        del gucian_creation_data['last_name']
        del gucian_creation_data['password']
        del gucian_creation_data['confirm_password']

        return Gucian.objects.create(**gucian_creation_data)
