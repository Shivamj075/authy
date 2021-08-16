from django.db import models

# Create your models here.
from authy.base.models import TimeStampedUUIDModel, Role
from authy.users.models import User


class OrganizationDetail(TimeStampedUUIDModel):
    name = models.CharField('Organization name', max_length=100)
    created_by = models.ForeignKey(User, related_name='organization_detail', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'OrganizationDetail'
        verbose_name_plural = 'OrganizationDetails'


class UserOrganization(TimeStampedUUIDModel):
    user = models.ForeignKey(User, related_name='user_organization', on_delete=models.CASCADE)
    organization = models.ForeignKey(OrganizationDetail, related_name='user_organization', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, related_name='user_organization', on_delete=models.CASCADE)
    is_active = models.BooleanField('is Active', default=True)

    class Meta:
        verbose_name = 'UserOrganization'
        verbose_name_plural = 'UserOrganizations'



# TODO need to add is_active in Organization Detail