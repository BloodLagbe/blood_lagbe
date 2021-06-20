from blog.models.post import Post
from django.db.models import Count


def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__name') \
        .annotate(Count('categories__name'))
    return queryset
