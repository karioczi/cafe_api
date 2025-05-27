from rest_framework.permissions import BasePermission, SAFE_METHODS #type:ignore

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    
class IsSelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user