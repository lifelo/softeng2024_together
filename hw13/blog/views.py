from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag

def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories, 'tags': tags})

def post_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories, 'tags': tags, 'current_category': category})

def post_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = Post.objects.filter(tags=tag)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories, 'tags': tags, 'current_tag': tag})



