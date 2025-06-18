
from django.contrib import admin
from django.urls import path
from blog.views import post_list, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", post_list, name="post-list"),
    path("post/<str:slug>/", post_detail, name="detail")
]
