from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 로그인한 사용자로 작성자 설정
            post.save()
            return redirect('post_list')  # 글 작성 후 글 목록 페이지로 리다이렉트
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})
