from django import forms       # Django의 폼 시스템 임포트
from .models import Task       # Task 모델 임포트

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task           # Task 모델을 기반으로 함
        fields = ['title', 'description', 'completed']  # 입력 필드 지정
