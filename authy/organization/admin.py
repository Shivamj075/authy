from django.contrib import admin

# Register your models here.
from authy.organization.models import OrganizationDetail, UserOrganization


@admin.register(OrganizationDetail)
class OrganizationDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by_id')


@admin.register(UserOrganization)
class OrganizationDetailAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'organization_id', 'role_id')