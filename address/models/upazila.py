from django.db import models

from address.models import District


class Upazila(models.Model):
    '''
        Upazila Model
    '''
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True
    )
    upazila_name = models.CharField(max_length=120)
    upazila_name_bn = models.CharField(max_length=120, blank=True, null=True)
    upazila_code = models.PositiveIntegerField(primary_key=True, blank=True)

    class Meta:
        ordering = ['upazila_name']

    def save(self, *args, **kwargs):
        if not self.upazila_code:
            if self.district.dist_code:
                last_upazila_code = Upazila.objects.filter(
                    district=self.district
                ).order_by('upazila_code').last()
                if last_upazila_code:
                    last_adding_code = int(
                        str(last_upazila_code.upazila_code)[3:]
                    )
                    if last_adding_code <= 8:
                        self.upazila_code = int(
                            str(self.district.dist_code) + '0' + str(
                                last_adding_code + 1
                            )
                        )
                    else:
                        self.upazila_code = int(
                            str(self.district.dist_code) + str(
                                last_adding_code + 1
                            )
                        )
                else:
                    self.upazila_code = int(
                        str(self.district.dist_code) + '01'
                    )
        super(Upazila, self).save(*args, **kwargs)

    def __str__(self):
        return self.upazila_name
