from django.urls import path
from .views import post_create

urlpatterns = [
    path('post/create/', post_create, name='post_create'),  # 글 작성 페이지
]
