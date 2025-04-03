from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Сортування від нового до старого
    return render(request, 'blog/post_list.html', {'posts': posts})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Повернення на головну сторінку після додавання
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('post_list')  # Повернення на головну сторінку після видалення
