# Generated by Django 3.2 on 2021-05-03 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood',
            name='donate_blood_to',
            field=models.CharField(blank=True, help_text='রক্ত দিতে পারবে', max_length=50, null=True, verbose_name='Donate Blood To'),
        ),
        migrations.AddField(
            model_name='blood',
            name='receive_blood_from',
            field=models.CharField(blank=True, help_text='রক্ত নিতে পারবে', max_length=50, null=True, verbose_name='Receive Blood From'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='code',
            field=models.CharField(blank=True, help_text='রক্তের কোড', max_length=50, null=True, verbose_name='Blood Group Code'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='group',
            field=models.CharField(blank=True, help_text='রক্তের গ্রুপ', max_length=50, null=True, verbose_name='Blood Group Name'),
        ),
        migrations.AlterField(
            model_name='blood',
            name='name',
            field=models.CharField(blank=True, help_text='রক্তের নাম', max_length=50, null=True, verbose_name='Blood Group Name'),
        ),
    ]
