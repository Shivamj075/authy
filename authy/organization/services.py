from authy.base import ENTITY_TYPE_ADMIN, ACCESS_TYPE_ADD_USER
from authy.base.models import Role
from authy.organization.models import UserOrganization, OrganizationDetail
from authy.organization.serializers import UserOrganizationDetailSerializer


def get_all_user_organizations(user):
    qs = UserOrganization.objects.filter(user=user, is_active=True).order_by('created_at')
    return UserOrganizationDetailSerializer(qs, many=True).data


def create_user_organization(user, name, role_id):
    organization = OrganizationDetail.objects.create(name=name, created_by=user)
    role = Role.objects.filter(id=role_id).first()
    UserOrganization.objects.create(user=user, organization=organization, role=role)


def update_user_in_organization(user, request_data):
    organization_id = request_data.get('org_id')
    user_id = request_data.get('user_id')
    role_id = request_data.get('role_id')
    qs = UserOrganization.objects.filter(user=user, organization_id=organization_id, is_active=True).first()
    if qs:
        role_access = qs.role.access.all().values_list('type')
        if ACCESS_TYPE_ADD_USER in role_access:
            obj, _ = UserOrganization.objects.update_or_create(user_id=user_id, organization_id=organization_id,
                                                               defaults={'role_id': role_id})
            return str(obj.id)
    return None
