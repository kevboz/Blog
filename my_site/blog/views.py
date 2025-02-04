from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.views import View
from django.urls import reverse





class starting_page(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-post_date"] # can add more ordering fields into this list
    context_object_name = "posts" # used so we can rename this object. normally this object is called "object" by default. This way we can call it "posts" in the html page

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# Create your views here.
# replaced with the above class view
# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-post_date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })
    


class AllPostsView(ListView):
    template_name = "blog/all-post.html"
    model = Post
    ordering = ["-post_date"] 
    context_object_name = "all_posts" # used so we can rename this object. normally this object is called "object" by default. This way we can call it "posts" in the html page

    # #the below isn't needed cause we aren't doing anything fancy. No Need to override it
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset


# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/all-post.html", {
#         "all_posts": all_posts
#     })


class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug) 
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form" : CommentForm()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug) 

        #save the post if it is valid
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # don't save to DB but create an object
            comment.post = post #save the new post object
            comment.save()
            HttpResponseRedirect(reverse("post_detail_page", args=[slug])) #redirect to the same page so we can view the comment we just add
            #this will issue a get request and load us on the right page. The slug is passed as part of the HTTP POST
        
        #form isn't valid. We need to load it and show the errors
        #Post = Post.objects.get(slug=slug) 
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form" : comment_form
        }
        return render(request, "blog/post-detail.html",context)

        



    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)

    #     #use the below to all an additional field to the data. This
    #     #this will get all post tags as part of the post object
    #     context["post_tags"] = self.object.tag.all()
    #     context["comment_form"] = CommentForm() # adds the comment form into our context so we can pass it along
    #     return context




#the below works but it doesn't accept a post

# class PostDetailView(DetailView):
#     # because the URLs file is setup to use the slug. The detailsview will 
#     # automatically search for it using the primary key. It will also give a 404 if 
#     # it doesn't find the record
#     #  path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post_detail_page'),
    
#     template_name = "blog/post-detail.html"
#     model = Post  
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)

#         #use the below to all an additional field to the data. This
#         #this will get all post tags as part of the post object
#         context["post_tags"] = self.object.tag.all()
#         context["comment_form"] = CommentForm() # adds the comment form into our context so we can pass it along
#         return context



# def post_detail(request, slug):
#     #identified_post = Post.objects.get(slug=slug) ## use this or
#     identified_post = get_object_or_404(Post, slug=slug)
    
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tag.all()
        
#     })
