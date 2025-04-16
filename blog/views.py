from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, content=content)
    return redirect('post_list')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('post_list')

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    session_key = request.session.session_key  # Отримуємо сесійний ключ користувача
    if not session_key:
        request.session.create()  # Якщо немає сесійного ключа, створюємо новий

    # Перевірка, чи вже є лайк для цього поста
    like, created = Like.objects.get_or_create(post=post, session_key=session_key)
    
    if not created:  # Якщо лайк уже існує, видаляємо його
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({'likes': post.like_count(), 'liked': liked})
