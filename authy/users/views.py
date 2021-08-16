from django.shortcuts import render

# Create your views here.

# TODO API FOR LIST OF ALL USERS and users which are not present in curr user organization
from rest_framework import viewsets, permissions, decorators
from rest_framework.response import Response

from authy.organization.models import UserOrganization
from authy.users.models import User
from authy.users.serializers import UserDetailSerializer


class UserDetailViewset(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = ''

    @decorators.action(methods=['get'], detail=False, url_path='all')
    def list_all_users(self, request, **kwargs):
        user = request.user
        if user is None:
            return Response({'status': False, 'reason': 'User must be logged In'})
        qs = User.objects.all()
        serializer = UserDetailSerializer(qs, many=True)
        if serializer.is_valid(raise_exception=True):
            return Response(data=serializer.data)
        return Response({'status': False, 'reason': serializer.errors})

    @decorators.action(methods=['get'], detail=False, url_path='all')
    def list_all_users_not_in_curr_organization(self, request, **kwargs):
        user = request.user
        if user is None:
            return Response({'status': False, 'reason': 'User must be logged In'})
        org_id = request.GET.get('id')
        qs = User.objects.all()
        curr_organization_users_id = UserOrganization.objects.filter(organization_id=org_id).values_list('user__id')
        qs = qs.exclude(id__in=curr_organization_users_id)
        serializer = UserDetailSerializer(qs, many=True)
        if serializer.is_valid(raise_exception=True):
            return Response(data=serializer.data)
        return Response({'status': False, 'reason': serializer.errors})