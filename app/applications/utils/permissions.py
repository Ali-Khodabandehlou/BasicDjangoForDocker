from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Gives permission only to the user related to the object
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Gives permission to eigther the user itself, or the superuser
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        return obj == request.user
