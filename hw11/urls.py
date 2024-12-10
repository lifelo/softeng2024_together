
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.task_list, name='task_list'),          # 작업 목록
    path('create/', views.task_create, name='task_create'),  # 작업 생성
    path('update/<int:pk>/', views.task_update, name='task_update'),  # 작업 수정
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('admin/', admin.site.urls),
    path('hw11/', include('hw11.my_to_do_app.urls')),  # my_to_do_
    # 작업 삭제
]

