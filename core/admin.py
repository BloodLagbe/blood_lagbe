from django.contrib import admin
from core.models import (Blood, Setting, Division, District, Upazila, Union,
                         Village)

# Register your models here.


class BloodAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'group',
                    'donate_blood_to',
                    'receive_blood_from')
    list_filter = ('code',)


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'slogan')
    list_filter = ('name',)


class DivisionModelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'name_bn', 'code', ]

    search_fields = [
        'name', 'name_bn', 'code'
    ]
    ordering = [
        'id'
    ]


class DistrictModelAdmin(admin.ModelAdmin):
    list_display = [
        'division', 'name', 'name_bn', 'code', ]

    search_fields = [
        'name', 'name_bn', 'code'
    ]
    ordering = [
        'name', 'name_bn'
    ]


class UpazilaModelAdmin(admin.ModelAdmin):
    list_display = [
        'division', 'district', 'name', 'name_bn', 'code', ]

    search_fields = [
        'name', 'name_bn', 'code'
    ]
    ordering = [
        'name', 'name_bn'
    ]

    def division(self, obj):
        return obj.district.division


class UnionModelAdmin(admin.ModelAdmin):
    list_display = [
        'division', 'district', 'upazila', 'name', 'name_bn', 'code', ]

    search_fields = [
        'name', 'name_bn', 'code'
    ]
    ordering = [
        'name', 'name_bn'
    ]

    def division(self, obj):
        return obj.upazila.district.division

    def district(self, obj):
        return obj.upazila.district


class VillageModelAdmin(admin.ModelAdmin):
    list_display = [
        'division', 'district', 'upazila', 'union', 'name', 'name_bn', 'code',
    ]

    search_fields = [
        'name', 'name_bn', 'code'
    ]
    ordering = [
        'name', 'name_bn'
    ]

    def division(self, obj):
        return obj.union.upazila.district.division

    def district(self, obj):
        return obj.union.upazila.district

    def upazila(self, obj):
        return obj.union.upazila


admin.site.register(Division, DivisionModelAdmin)
admin.site.register(District, DistrictModelAdmin)
admin.site.register(Upazila, UpazilaModelAdmin)
admin.site.register(Union, UnionModelAdmin)
admin.site.register(Village, VillageModelAdmin)
admin.site.register(Blood, BloodAdmin)
admin.site.register(Setting, SettingAdmin)
