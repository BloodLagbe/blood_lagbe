# Generated by Django 3.2 on 2021-07-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_profile_blood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='total_donate',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Total Blood Donate'),
        ),
    ]
