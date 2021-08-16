from django.contrib import admin

# Register your models here.
from authy.base.models import Access, Role


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')