from rest_framework.permissions import BasePermission


class IsProvider(BasePermission):
    message = "only providers can create and update a service"

    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role == "PROVIDER")

    def has_object_permission(self, request, view, obj):
        return obj.provider == request.user.provider_profile