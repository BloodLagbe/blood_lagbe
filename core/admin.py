from django.contrib import admin
from core.models import Blood, Setting

# Register your models here.


class BloodAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'group',
                    'donate_blood_to',
                    'receive_blood_from')
    list_filter = ('code',)


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'slogan')
    list_filter = ('name',)


admin.site.register(Blood, BloodAdmin)
admin.site.register(Setting, SettingAdmin)
