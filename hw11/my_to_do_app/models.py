from django.db import models  # Django의 데이터베이스 모델을 사용하기 위해 임포트

# Task 모델 정의
class Task(models.Model):
    title = models.CharField(max_length=255)      # 제목 필드 (문자열, 최대 길이 255)
    description = models.TextField(blank=True)    # 설명 필드 (긴 텍스트, 비워둘 수 있음)
    completed = models.BooleanField(default=False) # 완료 여부 필드 (True/False, 기본값 False)

    # 객체를 문자열로 표시할 때 사용할 메서드
    def __str__(self):
        return self.title  # 작업 제목을 반환


