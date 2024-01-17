from collections import OrderedDict

from django.conf import settings
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from users.models import UserModel


class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'phone_number')
        read_only_fields = ('id', 'first_name', 'last_name', 'phone_number')


class UserModelSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(region=settings.PHONE_NUMBER_REGION, required=True)
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    is_trainer = serializers.BooleanField(default=False)
    is_phone_number_verified = serializers.BooleanField(read_only=True, default=False)

    class Meta:
        model = UserModel
        fields = ('id', 'phone_number', 'first_name', 'last_name', 'is_trainer',
                  'is_phone_number_verified', 'student_parent_phone', 'student_parent_name',
                  'created_at', 'updated_at')

    def to_representation(self, instance: UserModel) -> OrderedDict:
        """Скрывает некоторые поля модели, в зависимости от типа пользователя"""

        ret = super(UserModelSerializer, self).to_representation(instance)
        if instance.is_trainer:
            for field in ('student_parent_phone', 'student_parent_name',):
                ret.pop(field)

        return ret

    def update(self, instance: UserModel, validated_data: dict) -> UserModel:
        if validated_data.get('phone_number'):
            instance.is_phone_number_verified = False

        return super(UserModelSerializer, self).update(instance, validated_data)

    def validate_phone_number(self, phone_number: str) -> str:
        if self.Meta.model.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('Пользователь с таким номером телефона уже существует.')
        return phone_number
