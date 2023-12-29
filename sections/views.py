from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from sections.models import SectionModel, GroupModel
from sections.serializer import SectionSerializer, GroupSerializer


class SectionViewSet(ModelViewSet):
    queryset = SectionModel.objects.all()
    serializer_class = SectionSerializer

    def get_permissions(self) -> list:
        method = self.request.method
        if method == 'POST':
            self.permission_classes = (IsAuthenticated,)
        elif method in ('PUT', 'PATCH', 'DELETE'):
            self.permission_classes = (IsAuthenticated,)

        return super(SectionViewSet, self).get_permissions()


class GroupViewSet(ModelViewSet):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
