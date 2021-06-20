from django.shortcuts import render


def postView(request, id):
    return render(request, 'blogapp/post.html', context={})