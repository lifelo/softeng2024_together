from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)  # 글 제목
    content = models.TextField()  # 글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 글 작성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 글 수정 시간
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 글 작성자 (로그인한 사용자)

    def __str__(self):
        return self.title
