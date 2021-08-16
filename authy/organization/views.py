from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, decorators
from rest_framework.response import Response

from authy.organization.serializers import UpdateUserOrganizationRequestSerializer, \
    CreateUserOrganizationRequestSerializer
from authy.organization.services import get_all_user_organizations, create_user_organization, \
    update_user_in_organization


class OrganizationDetailViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UpdateUserOrganizationRequestSerializer
    queryset = ''

    @decorators.action(methods=['get'], detail=False, url_path='all')
    def organization_list(self, request, **kwargs):
        user = request.user
        user_organization = get_all_user_organizations(user)
        return Response(data=user_organization)

    @decorators.action(methods=['post'], detail=False, url_path='create')
    def create_organization(self, request, **kwargs):
        user = request.user
        if user is None:
            return Response({'status': False, 'reason': 'User must be logged In'})
        serializer = CreateUserOrganizationRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data.get('name'))
            create_user_organization(user, serializer.data.get('org_name'), serializer.data.get('role_id'))
        return Response({'status': True})

    @decorators.action(methods=['post'], detail=False, url_path='update')
    def update_users_in_organization(self, request, **kwargs):
        user = request.user
        if user is None:
            return Response({'status': False, 'reason': 'User must be logged In'})
        serializer = UpdateUserOrganizationRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request_data = {}
            request_data.update({'user_id': serializer.data.get('user_id')})
            request_data.update({'org_id': serializer.data.get('org_id')})
            request_data.update({'role_id': serializer.data.get('role_id')})

            _result = update_user_in_organization(user, request_data)
            if _result:
                return Response({'status': True})
            return Response({'status': False, 'reason': 'User Dont have permission to do so'})
        return Response({'status': False, 'reason': serializer.errors})