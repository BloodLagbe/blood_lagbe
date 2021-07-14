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
    group = models.CharField(
        _("Blood Group Name"), max_length=50, blank=True, null=True,
        help_text='রক্তের গ্রুপ'
    )
    donate_blood_to = models.CharField(_("Donate Blood To"),
                                       max_length=50, blank=True, null=True,
                                       help_text='রক্ত দিতে পারবে')
    receive_blood_from = models.CharField(_("Receive Blood From"),
                                          max_length=50, blank=True, null=True,
                                          help_text='রক্ত নিতে পারবে')

    def __str__(self):
        return str(self.name)


class Setting(models.Model):
    name = models.CharField(
        _("System Name"), max_length=50, blank=True,
        null=True, help_text='সিস্টেম এর নাম'
    )
    logo = models.FileField(
        _("System logo"), upload_to="media/logo/", max_length=100, blank=True,
        null=True, help_text='সিস্টেম এর প্রতিক'
    )
    slogan = models.CharField(
        _("Slogan for system"), max_length=100, blank=True, null=True,
        help_text='সিস্টেম এর স্লগান'
    )
