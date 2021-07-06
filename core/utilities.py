import os
import csv
from django.shortcuts import render
from .models import (Division, District, Upazila, Union, Village)


def division_import(request):
    """ 
    function for import division
    """

    if request.POST:
        pwd = os.path.dirname(__file__)
        with open(pwd + '/csv/divisions.csv', encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            num = 0
            for row in reader:
                obj, created = Division.objects.get_or_create(
                    name=row['divi_name'],
                    name_bn=row['divi_name_bn'],
                    code=row['divi_code']
                )
                num += 1
                print(f'serial={num}, object={obj}, created={created}')

    return render(request, "importdata/import_division.html")


def district_import(request):
    """ 
    function for import district
    """

    if request.POST:
        pwd = os.path.dirname(__file__)
        with open(pwd + '/csv/data.csv', encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            count = 0
            for row in reader:
                code = row['district_code'].strip()
                code_division = row['division_code'].strip()
                name = row['district_name'].strip()
                name_bn = row['district_name_bn'].strip()

                district = District.objects.filter(
                    code=code, name=name,
                    division__code=code_division
                )
                if not district:
                    division = Division.objects.filter(code=code_division)
                    if division:
                        divisions = division[0]
                    else:
                        divisions = Division(code=code_division)
                        divisions.save()
                    created_district = District(
                        division=divisions,
                        code=code,
                        name=name,
                        name_bn=name_bn
                    )
                    created_district.save()
                else:
                    print("existing---", district)
                count = count + 1
                print(count)
    return render(request, "importdata/import_district.html")


def upazila_import(request):
    """ 
    function for import upazila 
    """

    if request.POST:
        pwd = os.path.dirname(__file__)
        with open(pwd + '/csv/data.csv', encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            count = 0
            for row in reader:
                code = row['upazila_code'].strip()
                code_district = row['district_code'].strip()
                code_division = row['division_code'].strip()
                name = row['upazila_name'].strip()
                name_bn = row['upazila_name_bn'].strip()
                upazila = Upazila.objects.filter(
                    code=code, name=name,
                    district__code=code_district,
                    district__division__code=code_division
                )
                if not upazila:
                    district = District.objects.filter(
                        code=code_district, division__code=code_division)
                    if district:
                        districts = district[0]
                    else:
                        districts = District(
                            code=code_district,
                            division__code=code_division)
                        districts.save()
                    created_upazila = Upazila(
                        district=districts,
                        code=code,
                        name=name,
                        name_bn=name_bn
                    )
                    created_upazila.save()
                else:
                    print("existing---", upazila)
                count = count + 1
                print(count)
    return render(request, "importdata/import_upazila.html")


def union_import(request):
    """ 
    function for import union 
    """

    if request.POST:
        pwd = os.path.dirname(__file__)
        with open(pwd + '/csv/data.csv', encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            count = 0
            for row in reader:
                code = row['union_code'].strip()
                code_upazila = row['upazila_code'].strip()
                code_district = row['district_code'].strip()
                code_division = row['division_code'].strip()
                name = row['union_name'].strip()
                name_bn = row['union_name_bn'].strip()
                union = Union.objects.filter(
                    code=code, name=name,
                    upazila__code=code_upazila,
                    upazila__district__code=code_district,
                    upazila__district__division__code=code_division
                )
                if not union:
                    upazila = Upazila.objects.filter(
                        code=code_upazila, district__code=code_district,
                        district__division__code=code_division)
                    if upazila:
                        upazilas = upazila[0]
                    else:
                        upazilas = Upazila(
                            code=code_upazila,
                            district__code=code_district,
                            district__division__code=code_division)
                        upazilas.save()
                    created_union = Union(
                        upazila=upazilas,
                        code=code,
                        name=name,
                        name_bn=name_bn
                    )
                    created_union.save()
                else:
                    print("existing---", union)
                count = count + 1
                print(count)
    return render(request, "importdata/import_union.html")


def village_import(request):
    """ 
    function for import village
    """

    if request.POST:
        pwd = os.path.dirname(__file__)
        with open(pwd + '/csv/data.csv', encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            count = 0
            for row in reader:
                code = row['village_code'].strip()
                code_union = row['union_code'].strip()
                name_union = row['union_name'].strip()
                code_upazila = row['upazila_code'].strip()
                code_district = row['district_code'].strip()
                code_division = row['division_code'].strip()
                name = row['village_name'].strip()
                name_bn = row['village_name_bn'].strip()
                village = Village.objects.filter(
                    code=code, name=name,
                    union__code=code_union, union__name=name_union,
                    union__upazila__code=code_upazila,
                    union__upazila__district__code=code_district,
                    union__upazila__district__division__code=code_division
                )
                if not village:
                    union = Union.objects.filter(
                        code=code_union, name=name_union,
                        upazila__code=code_upazila,
                        upazila__district__code=code_district,
                        upazila__district__division__code=code_division)
                    if union:
                        unions = union[0]
                    else:
                        unions = Union(
                            code=code_union, name=name_union,
                            upazila__code=code_upazila,
                            upazila__district__code=code_district,
                            upazila__district__division__code=code_division,
                        )
                        unions.save()
                    created_village = Village(
                        union=unions,
                        code=code,
                        name=name,
                        name_bn=name_bn
                    )
                    created_village.save()
                else:
                    print("existing---", village)
                count = count + 1
                print(count)
    return render(request, "importdata/import_village.html")
