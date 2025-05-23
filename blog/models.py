from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Для зображення
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)  # Для відео
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def like_count(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()  # тільки контент без імені
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # показує перші 50 символів контенту

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)  # унікально для сесії

    class Meta:
        unique_together = ('post', 'session_key')
