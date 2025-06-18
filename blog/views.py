from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
from django.db.models import Q

def post_list(request):
    posts = Post.objects.all()
    if request.GET.get("search"):
        search = request.GET.get("search")
        posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post.html", {"post": post})
