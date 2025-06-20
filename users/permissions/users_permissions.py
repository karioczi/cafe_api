from rest_framework.permissions import BasePermission, SAFE_METHODS #type:ignore

class IsAllowAny(BasePermission):
    def has_permission(self, request, view):
        return True

class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS    

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated
        )
    
class IsClient(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and 
            request.user.role == 'client'
        )

class IsSelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_authenticated and (
            request.user.role == 'admin' or
            obj == request.user
            )
        )

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and
            request.user.role =='admin'
        )

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsAdminOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and (
            request.user.is_staff or 
            request.user.is_superuser
        )