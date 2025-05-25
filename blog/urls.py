from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add/', views.add_post, name='add_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),

    # Реєстрація користувача
    path('register/', views.register, name='register'),

    # Профіль користувача — перегляд і редагування
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    # Вбудовані маршрути для авторизації (login, logout, password reset і т.д.)
    path('accounts/', include('django.contrib.auth.urls')),
]
