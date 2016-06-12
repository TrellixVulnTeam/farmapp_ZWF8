from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email',)
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = (
#             'first_name',
#             'last_name',
#             'username',
#             'password',
#             'email',
#         )
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }

#     def create(self, validated_data):
#         user = get_user_model().objects.create_user(**validated_data)
#         return user

#     def update(self, instance, validated_data):
#         if 'password' in validated_data:
#             password = validated_data.pop('password')
#             instance.set_password(password)
#         return super(UserSerializer, self).update(instance, validated_data)