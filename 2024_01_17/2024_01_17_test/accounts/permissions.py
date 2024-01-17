from rest_framework.permissions import BasePermission

class DevicePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.device_permission