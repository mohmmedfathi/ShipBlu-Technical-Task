from django.conf import settings
from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        if view.action == 'create':
            return request.user and request.user.is_authenticated

        return True

    def has_object_permission(self, request, view, obj):
        is_admin = request.user.is_staff or \
            request.user.role == settings.AUTH_USER_MODEL.Roles.ADMIN

        if request.method in permissions.SAFE_METHODS:
            return obj.customer == request.user or is_admin

        return obj.customer == request.user or is_admin
