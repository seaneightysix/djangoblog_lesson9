from django.urls import path
from myblog.views import list_view, detail_view, add_post

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('myblog/<int:post_id>/', detail_view, name="blog_detail"),
    path('myblog/addpost/', add_post, name="add_post")

]