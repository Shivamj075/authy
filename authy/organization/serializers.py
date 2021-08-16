from rest_framework import serializers

from authy.organization.models import OrganizationDetail, UserOrganization
from authy.users.serializers import UserDetailSerializer


class OrganizationDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = OrganizationDetail
        fields = ['id', 'name']


class UserOrganizationDetailSerializer(serializers.ModelSerializer):
    organization = OrganizationDetailSerializer()

    class Meta:
        model = UserOrganization
        fields = ['id', 'name']


class UpdateUserOrganizationRequestSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    org_id = serializers.CharField()
    role_id = serializers.CharField()


class CreateUserOrganizationRequestSerializer(serializers.Serializer):
    org_name = serializers.CharField()
    role_id = serializers.CharField()