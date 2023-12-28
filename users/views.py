from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from users.models import StudentModel, TrainerModel, UserModel
from users.permissions import (
    IsOwnerOrStaff, IsGroupTrainerOrAccountOwnerOrStaff, IsSectionOwner)
from users.serializer import (StudentModelSerializer, TrainerModelSerializer,
                              UserModelSerializer)


class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def get_permissions(self) -> list:
        method = self.request.method
        if method == 'POST':
            self.permission_classes = (AllowAny,)
        elif method in ('GET', 'PUT', 'PATCH'):
            self.permission_classes = (IsOwnerOrStaff,)
        elif method == 'DELETE':
            self.permission_classes = (IsAdminUser,)

        return super(UserViewSet, self).get_permissions()


class TrainerViewSet(UserViewSet):
    queryset = TrainerModel.objects.all()
    serializer_class = TrainerModelSerializer

    def get_permissions(self) -> list:
        return super().get_permissions()


class StudentViewSet(UserViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

    def get_permissions(self) -> list:
        method = self.request.method
        if method == 'POST':
            self.permission_classes = (AllowAny,)
        elif method in ('GET', 'PUT', 'PATCH'):
            self.permission_classes = (IsGroupTrainerOrAccountOwnerOrStaff, IsSectionOwner)
        elif method == 'DELETE':
            self.permission_classes = (IsAdminUser,)

        return super(StudentViewSet, self).get_permissions()
