from django.contrib import admin

# Register your models here.
from authy.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active')