from rest_framework import permissions


class UpdateOwnerProfile(permissions.BasePermission):
    """Allow users to edit own profiles"""

    def has_object_permission(self, request, view, obj):
        """check user trying to edit thier own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
