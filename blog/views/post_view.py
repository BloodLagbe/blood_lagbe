from django.shortcuts import render


def postView(request, id):
    return render(request, 'blog/blog.html', context={})