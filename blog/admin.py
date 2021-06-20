from django.contrib import admin
from .models.author import Author
from .models.category import Category
from .models.post import Post


# Register your models here.


class AuthorAdmin(admin.ModelAdmin):

    list_display = [
        'admin_photo',
        'author',
    ]

class PostAdmin(admin.ModelAdmin):

    list_display = [
        'admin_photo',
        'title',
        'timestamp',
        'comment_count',
        'view_count',
        'author',
        'featured'
    ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)

