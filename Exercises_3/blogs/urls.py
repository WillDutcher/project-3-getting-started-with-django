"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Page that shows page for a specific topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new post.
    path('new_post/<int:topic_id>/', views.new_post, name='new_post'),
    # Page for editing a post.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    # Page that shows all posts.
    path('posts/', views.posts, name='posts'),
]
