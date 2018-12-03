from rest_framework import serializers

from ..models import Gucian


class GucianRetrieveSerializer(serializers.ModelSerializer):
    """
    Validation for retrieve action on Gucian Model data.

    Author: Abdelrahmen Ayman
    """
    class Meta:
        model = Gucian
        fields = ('guc_email', 'backup_email', 'major', 'dash_number',
                  'birthdate', 'bio', 'reputation', 'name', 'age')


class GucianUpdateSerializer(serializers.ModelSerializer):
    """
    Validation for update action on Gucian Model data.

    Author: Abdelrahmen Ayman
    """
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = Gucian
        fields = ('backup_email', 'major', 'dash_number',
                  'birthdate', 'bio', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        """
        Update instance.user related fields.

        Author: Abdelrahmen Ayman
        """
        user_related_keys = ['first_name', 'last_name']

        for key in user_related_keys:
            if key in self.initial_data.keys():
                setattr(instance.user, key, self.initial_data[key])
        instance.user.save()

        return super().update(instance, validated_data)

    def get_first_name(self, gucian):
        return self._get_field_new_value(
            key='first_name',
            default=gucian.user.first_name)

    def get_last_name(self, gucian):
        return self._get_field_new_value(
            key='last_name',
            default=gucian.user.last_name)

    def _get_field_new_value(self, key, default):
        """
        Checks if key exists in validated data, if not it returns
        the default given value.

        Author: Abdelrahmen Ayman
        """
        if key in self.initial_data.keys():
            return self.initial_data[key]
        return default
