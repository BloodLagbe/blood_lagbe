from django.db import models
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe


class Author(models.Model):
    User = get_user_model()
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post', default='no_pic.jpg')

    def __str__(self):
        return str(self.author)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
