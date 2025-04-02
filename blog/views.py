from django.shortcuts import render, redirect
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
