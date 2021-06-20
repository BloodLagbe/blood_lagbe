from django.db import models
from .author import Author
from .category import Category
from django.utils.safestring import mark_safe
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    overview = models.TextField()
    thumbnail = models.ImageField(upload_to='post', default='no_image.jpeg')
    view_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.thumbnail.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def get_absolute_url(self):
        return reverse('post-view', kwargs={
            'id': self.id,
        })

