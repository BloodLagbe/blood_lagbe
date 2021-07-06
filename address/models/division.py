from django.db import models


class Division(models.Model):
    '''
        Division Model
    '''
    div_name = models.CharField(max_length=120)
    div_name_bn = models.CharField(max_length=120, blank=True, null=True)
    div_code = models.PositiveIntegerField(primary_key=True)

    class Meta:
        ordering = ['div_name']

    def __str__(self):
        return self.div_name
