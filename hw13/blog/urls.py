from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 게시글 리스트
    path('category/<int:category_id>/', views.post_by_category, name='post_by_category'),  # 카테고리별 게시글
    path('tag/<int:tag_id>/', views.post_by_tag, name='post_by_tag'),  # 태그별 게시글
]
