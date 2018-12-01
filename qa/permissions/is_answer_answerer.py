from rest_framework import permissions


class IsAnswerAnswerer(permissions.BasePermission):
    """
    Object-level permission to allow answer answerer only
    to make changes to the object.
    """

    def has_object_permission(self, request, view, answer):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == answer.answerer.user:
            return True
        return False
