from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email','is_superuser','is_staff']
    ordering = ['email']

    fieldsets = (
        ("Authentication", {
            "fields": (
                'email','password'
            ),
        }),
        ("Permission", {
            "fields":(
                "is_superuser", "is_staff", "is_active",
            ),
        }),
        ("Group Permission", {
            "fields":(
                "groups", "user_permissions",
            ),
        }),
        ("Important_date", {
            "fields":(
                "last_login",
            ),
        }),
    )

    add_fieldsets = (
        ('From', {
            "fields": (
                'email','password1','password2','is_staff','is_superuser','is_active',
            ),
        }),
    )

admin.site.register(User,CustomUserAdmin)