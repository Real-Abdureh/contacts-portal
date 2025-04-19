from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'full_name', 'contact_number', 'is_staff')
    search_fields = ('username', 'email', 'full_name', 'contact_number')
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'contact_number')}),
    )

admin.site.register(User, UserAdmin)
