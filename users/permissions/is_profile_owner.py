from rest_framework import permissions


class IsProfileOwner(permissions.BasePermission):
    """
    Object-level permission to allow profile owner only
    to make changes to the object.

    Author: Abdelrahmen Ayman
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == obj.user:
            return True
        return False
