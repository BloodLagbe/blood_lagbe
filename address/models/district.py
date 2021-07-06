from django.db import models

from address.models import Division


class District(models.Model):
    '''
        District Model
    '''
    division = models.ForeignKey(
        Division, on_delete=models.SET_NULL, null=True
    )
    dist_name = models.CharField(max_length=120)
    dist_name_bn = models.CharField(max_length=120, blank=True, null=True)
    dist_code = models.PositiveIntegerField(primary_key=True, blank=True)

    class Meta:
        ordering = ['dist_name']

    def save(self, *args, **kwargs):
        if not self.dist_code:
            if self.division.div_code:
                last_dist_code = District.objects.filter(
                    division=self.division
                ).order_by('dist_code').last()
                if last_dist_code:
                    last_adding_code = int(str(last_dist_code.dist_code)[1:])
                    if last_adding_code <= 8:
                        self.dist_code = int(
                            str(self.division.div_code) + '0' + str(
                                last_adding_code + 1
                            )
                        )
                    else:
                        self.dist_code = int(
                            str(self.division.div_code) + str(
                                last_adding_code + 1
                            )
                        )
                else:
                    self.dist_code = int(str(self.division.div_code) + '01')
        super(District, self).save(*args, **kwargs)

    def __str__(self):
        return self.dist_name
