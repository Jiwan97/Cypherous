from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .models import User


class UserAdmin(BaseAdmin):
    fieldsets = (
        *BaseAdmin.fieldsets,
        (
            'Verification',
            {
                'fields': (
                    'is_email_verified',
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
