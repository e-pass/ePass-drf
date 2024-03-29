from typing import Any

from django.views import View
from rest_framework import permissions
from rest_framework.request import Request


class IsOwnerOrStaff(permissions.BasePermission):
    """Права на аккаунт для владельца аккаунта или администратора"""

    def has_object_permission(self, request: Request, view: View, obj: Any) -> bool:
        return any((obj.id == request.user.id, request.user.is_staff))


class IsSectionOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Any) -> bool:
        return request.user.id == obj.owner_id


class IsGroupTrainerOrAccountOwnerOrStaff(permissions.BasePermission):
    """Права на аккаунт для владельца секции(если аккаунт подписан к секции),
        тренеров групп(если аккаунт подписан к группам),
        владельца аккаунта или администратора"""

    def has_object_permission(self, request: Request, view: View, obj: Any) -> bool:
        group_trainers = []
        if obj.my_groups:
            group_trainers = [group.trainer.id for group in obj.my_groups.all()]
        return any((
            request.user.id in group_trainers,
            obj.id == request.user.id, request.user.is_staff
        ))


class IsTrainer(permissions.BasePermission):
    """Простая проверка, является ли пользователь тренером"""

    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_trainer


class IsPassStudentOrTrainerOrSectionOwner(permissions.BasePermission):
    """Права на абонемент для студента, тренера или владельца секции"""

    def has_object_permission(self, request: Request, view: View, obj: Any) -> bool:
        return any((request.user == obj.student, request.user in obj.section.trainers.all(),
                    request.user == obj.section.owner))


class IsTrainerOrSectionOwner(permissions.BasePermission):
    """Права на абонемент для тренера или владельца секции"""

    def has_object_permission(self, request: Request, view: View, obj: Any) -> bool:
        return any((request.user in obj.section.trainers.all(),
                    request.user == obj.section.owner))
