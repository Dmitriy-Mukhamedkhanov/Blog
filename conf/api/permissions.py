from rest_framework.permissions import BasePermission


class IsAuthorObject(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj or request.method == 'GET')
