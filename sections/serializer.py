from rest_framework import serializers

from sections.models import GroupModel, SectionModel
from users.models import UserModel
from users.serializer import UserModelSerializer


class ShortSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SectionModel
        fields = ('id', 'title', 'created_at', 'updated_at',)


class GroupSerializer(serializers.ModelSerializer):
    trainers_ids = serializers.PrimaryKeyRelatedField(
        source='trainers',
        queryset=UserModel.trainers.all(),
        write_only=True,
        required=False,
        many=True
    )
    students_ids = serializers.PrimaryKeyRelatedField(
        source='students',
        queryset=UserModel.students.all(),
        write_only=True,
        required=False,
        many=True
    )

    trainers = UserModelSerializer(many=True, read_only=True)
    students = UserModelSerializer(many=True, read_only=True)

    def validate_trainers_ids(self, values: list[int]) -> list[int]:
        section_id = self.context['view'].kwargs.get('section_id')
        section = SectionModel.objects.get(id=section_id)
        trainers = section.trainers.all()
        for train in values:
            if train not in trainers:
                raise serializers.ValidationError('Тренер не состоит в секции')

        return values

    class Meta:
        model = GroupModel
        fields = ('id', 'title', 'trainers', 'trainers_ids',
                  'students', 'students_ids',
                  'created_at', 'updated_at')


class ShortGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupModel
        fields = ('id', 'title', 'created_at', 'updated_at',)


class SectionSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(
        source='owner',
        queryset=UserModel.trainers.all(),
        write_only=True,
        error_messages={
            'does_not_exist': 'Пользователь не зарегистрирован или не является тренером'}
    )
    trainers_ids = serializers.PrimaryKeyRelatedField(
        source='trainers',
        queryset=UserModel.trainers.all(),
        write_only=True,
        required=False,
        many=True
    )

    owner = UserModelSerializer(read_only=True)
    trainers = UserModelSerializer(many=True, read_only=True)
    groups = ShortGroupSerializer(many=True, read_only=True)

    class Meta:
        model = SectionModel
        fields = '__all__'
