from django.shortcuts import render, get_object_or_404
from .models import Post



# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-post_date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })
    

def posts(request):
    all_posts = Post.objects.all()
    return render(request, "blog/all-post.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    #identified_post = Post.objects.get(slug=slug) ## use this or
    identified_post = get_object_or_404(Post, slug=slug)
    print (slug)
    print (identified_post)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })