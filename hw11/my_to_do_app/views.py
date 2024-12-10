from django.shortcuts import render, redirect  # 요청 처리와 리디렉션을 위해 임포트
from .models import Task                       # Task 모델 임포트
from .forms import TaskForm                    # TaskForm 임포트

# 작업 목록 뷰
def task_list(request):
    tasks = Task.objects.all()                # 데이터베이스에서 모든 Task 객체를 가져옴
    return render(request, 'my_to_do_app/task_list.html', {'tasks': tasks})

# 작업 생성 뷰
def task_create(request):
    if request.method == 'POST':              # 사용자가 데이터를 제출했을 때
        form = TaskForm(request.POST)         # 전송된 데이터로 폼 생성
        if form.is_valid():                   # 데이터가 유효한지 검사
            form.save()                       # 데이터 저장
            return redirect('task_list')      # 작업 목록으로 리디렉션
    else:
        form = TaskForm()                     # 빈 폼 생성
    return render(request, 'my_to_do_app/task_form.html', {'form': form})

# 작업 수정 뷰
def task_update(request, pk):
    task = Task.objects.get(pk=pk)            # pk로 특정 작업 가져오기
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # 기존 데이터를 폼에 연결
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'my_to_do_app/task_form.html', {'form': form})

# 작업 삭제 뷰
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':              # 삭제 요청 확인
        task.delete()                         # 작업 삭제
        return redirect('task_list')
    return render(request, 'my_to_do_app/task_confirm_delete.html', {'task': task})



