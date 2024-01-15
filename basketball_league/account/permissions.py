from rest_framework.permissions import BasePermission

from .models import Role


class IsCoach(BasePermission):
    def has_object_permission(self, request):
        return request.user.role.name == Role.coach
    
class IsLeagueAdmin(BasePermission):
    def has_object_permission(self, request):
        return request.user.role.name == Role.league_admin
    
class IsCoachOrLeagueAdmin(BasePermission):
    def has_object_permission(self, request):
        return request.user.role.name == Role.league_admin or request.user.role.name == Role.coach