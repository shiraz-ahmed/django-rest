from rest_framework import permissions


class update_own_profile(permissions.BasePermission):
    """creating permissions so that the only person to update his account is himself """
    def has_object_permission(self, request, view, obj):

        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class update_own_status(permissions.BasePermission):
    """allow user to update their status"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id== request.user.id
