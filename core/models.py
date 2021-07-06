from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Blood(models.Model):
    name = models.CharField(_("Blood Group Name"),
                            max_length=50, blank=True, null=True,
                            help_text='রক্তের নাম')
    code = models.CharField(_("Blood Group Code"),
                            max_length=50, blank=True, null=True,
                            help_text='রক্তের কোড')
    group = models.CharField(_("Blood Group Name"),
                             max_length=50, blank=True, null=True,
                             help_text='রক্তের গ্রুপ')
    donate_blood_to = models.CharField(_("Donate Blood To"),
                                       max_length=50, blank=True, null=True,
                                       help_text='রক্ত দিতে পারবে')
    receive_blood_from = models.CharField(_("Receive Blood From"),
                                          max_length=50, blank=True, null=True,
                                          help_text='রক্ত নিতে পারবে')

    def __str__(self):
        return str(self.name)


class Setting(models.Model):
    name = models.CharField(_("System Name"),
                            max_length=50, blank=True, null=True,
                            help_text='সিস্টেম এর নাম')
    logo = models.FileField(_("System logo"),
                            upload_to="media/logo/",
                            max_length=100, blank=True, null=True,
                            help_text='সিস্টেম এর প্রতিক')
    slogan = models.CharField(_("Slogan for system"),
                              max_length=100, blank=True, null=True,
                              help_text='সিস্টেম এর স্লগান')


class Division(models.Model):
    """
    Division model
    """

    name = models.CharField(max_length=100, blank=False, null=True)

    name_bn = models.CharField(max_length=100, blank=False, null=True)

    code = models.CharField(max_length=10, blank=False, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class District(models.Model):
    """
    District model
    """

    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, blank=False, null=True,)

    name = models.CharField(max_length=100, blank=False, null=True)

    name_bn = models.CharField(max_length=100, blank=False, null=True)

    code = models.CharField(max_length=10, blank=False, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Upazila(models.Model):
    """
    Upazila model
    """

    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, blank=False, null=True,)

    name = models.CharField(max_length=100, blank=False, null=True)

    name_bn = models.CharField(max_length=100, blank=False, null=True)

    code = models.CharField(max_length=10, blank=False, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Union(models.Model):
    """
    Union model
    """

    upazila = models.ForeignKey(
        Upazila, on_delete=models.SET_NULL, blank=False, null=True,)

    name = models.CharField(max_length=100, blank=False, null=True)

    name_bn = models.CharField(max_length=100, blank=False, null=True)

    code = models.CharField(max_length=10, blank=False, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Village(models.Model):
    """
    Village model
    """

    union = models.ForeignKey(
        Union, on_delete=models.SET_NULL, blank=False, null=True,)

    name = models.CharField(max_length=100, blank=False, null=True)

    name_bn = models.CharField(max_length=100, blank=False, null=True)

    code = models.CharField(max_length=10, blank=False, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
