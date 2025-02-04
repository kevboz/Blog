from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page.as_view(),name="starting-page"),
    path('posts', views.AllPostsView.as_view(), name='posts_page'),
    path('posts/<slug:slug>', views.SinglePostView.as_view(), name='post_detail_page')
]
