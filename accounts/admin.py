from django.contrib import admin
from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts import models

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone',
                    'is_active', 'is_staff'
                    ]

    list_filter = ['admin']

    search_fields = ['id', 'email', 'first_name', 'last_name', 'phone']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(models.Profile)
