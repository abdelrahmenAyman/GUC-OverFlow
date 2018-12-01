from rest_framework import permissions


class IsQuestionAsker(permissions.BasePermission):
    """
    Object-level permission to allow question asker only
    to make changes to the object.
    """

    def has_object_permission(self, request, view, question):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == question.asker.user:
            return True
        return False
