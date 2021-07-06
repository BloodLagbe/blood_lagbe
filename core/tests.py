from django.test import TestCase
from .models import (Division, District, Upazila, Union, Village)
# Create your tests here.


class DivisionModelTest(TestCase):
    """ 
    Division create & str test 
    """

    def setUp(self):
        Division.objects.create(name='Dhaka', name_bn='ঢাকা', code='10',)

    def test_name_content(self):
        division = Division.objects.get(id=1)
        expected_object_name = f'{division.name}'
        self.assertEqual(expected_object_name, 'Dhaka')


class DistrictModelTest(TestCase):
    """ 
    District create & str test 
    """

    def setUp(self):
        self.division = Division.objects.create(
            name='Dhaka',
            name_bn='ঢাকা',
            code='10',
        )

        District.objects.create(
            division=self.division,
            name='Dhaka',
            name_bn='ঢাকা',
            code='10',
        )

    def test_name_content(self):
        district = District.objects.get(id=1)
        expected_object_name = f'{district.name}'
        self.assertEqual(expected_object_name, 'Dhaka')


class UpazilaModelTest(TestCase):
    """ 
    Upazila create & str test
    """

    def setUp(self):
        self.district = District.objects.create(
            name='Dhaka',
            name_bn='ঢাকা',
            code='10',
        )

        Upazila.objects.create(
            district=self.district,
            name='Mirpur',
            name_bn='মিরপুর',
            code='11',
        )

    def test_name_content(self):
        upazila = Upazila.objects.get(id=1)
        expected_object_name = f'{upazila.name}'
        self.assertEqual(expected_object_name, 'Mirpur')


class UnionModelTest(TestCase):
    """ 
    Union create & str test 
    """

    def setUp(self):
        self.upazila = Upazila.objects.create(
            name='Mirpur',
            name_bn='মিরপুর',
            code='11',
        )

        Union.objects.create(
            upazila=self.upazila,
            name='Mirpur',
            name_bn='মিরপুর',
            code='11',
        )

    def test_name_content(self):
        union = Union.objects.get(id=1)
        expected_object_name = f'{union.name}'
        self.assertEqual(expected_object_name, 'Mirpur')


class VillageModelTest(TestCase):
    """ 
    Village create & str test 
    """

    def setUp(self):
        self.union = Union.objects.create(
            name='Mirpur',
            name_bn='মিরপুর',
            code='11',
        )

        Village.objects.create(
            union=self.union,
            name='Kollapathor',
            name_bn='কোল্লাপাথর',
            code='3500',
        )

    def test_name_content(self):
        village = Village.objects.get(id=1)
        expected_object_name = f'{village.name}'
        self.assertEqual(expected_object_name, 'Kollapathor')
