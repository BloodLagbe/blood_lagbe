from django.contrib import admin
from import_export import resources
from import_export.admin import (
    ImportExportModelAdmin, ImportExportActionModelAdmin
)

from address.models import Division, District, Upazila


class DivisionResource(resources.ModelResource):
    class Meta:
        model = Division


class DistrictResource(resources.ModelResource):
    class Meta:
        model = District


class UpazilaResource(resources.ModelResource):
    class Meta:
        model = Upazila


class DivisionAdmin(
    ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin
):
    list_display = ['div_name', 'div_name_bn', 'div_code']
    resource_class = DivisionResource


class DistrictAdmin(
    ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin
):
    list_display = [
        'division', 'dist_name', 'dist_name_bn', 'dist_code'
    ]
    list_filter = ['division']
    search_fields = ['dist_name', 'dist_name_bn', 'dist_code']
    readonly_fields = ['dist_code']
    resource_class = DistrictResource


class UpazilaAdmin(
    ImportExportModelAdmin, ImportExportActionModelAdmin, admin.ModelAdmin
):
    list_display = [
        'district', 'upazila_name', 'upazila_name_bn', 'upazila_code'
    ]
    list_filter = ['district']
    search_fields = ['upazila_name', 'upazila_name_bn', 'upazila_code']
    readonly_fields = ['upazila_code']
    resource_class = UpazilaResource


admin.site.register(Division, DivisionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Upazila, UpazilaAdmin)
