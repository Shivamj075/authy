from rest_framework import serializers

from authy.users.models import User


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']