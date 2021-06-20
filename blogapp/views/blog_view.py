from django.shortcuts import render
from blogapp.models.post import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .category_count_view import get_category_count


def blogView(request):
    category_count = get_category_count()
    latest_post = Post.objects.order_by('-timestamp')[0:3]
    blog_list = Post.objects.all()
    paginator = Paginator(blog_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'category_count': category_count,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'latest_post': latest_post,
    }
    return render(request, 'blogapp/blog.html', context)
