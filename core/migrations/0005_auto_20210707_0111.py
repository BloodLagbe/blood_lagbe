# Generated by Django 3.2 on 2021-07-06 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210706_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='union',
            name='upazila',
        ),
        migrations.RemoveField(
            model_name='upazila',
            name='district',
        ),
        migrations.RemoveField(
            model_name='village',
            name='union',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Division',
        ),
        migrations.DeleteModel(
            name='Union',
        ),
        migrations.DeleteModel(
            name='Upazila',
        ),
        migrations.DeleteModel(
            name='Village',
        ),
    ]
