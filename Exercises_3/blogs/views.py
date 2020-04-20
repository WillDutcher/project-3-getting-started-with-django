from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Post
from .forms import TopicForm, PostForm

def index(request):
    """The home page for Blogs."""
    return render(request, 'blogs/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blogs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)

    posts = topic.post_set.order_by('-date_added')
    context = {'topic': topic, 'posts': posts}
    return render(request, 'blogs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('blogs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_topic.html', context)

def posts(request):
    """Show all posts."""
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    print("TESTING 1 2 3")
    return render(request, 'blogs/posts.html', context)

@login_required
def new_post(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.topic = topic
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = Post.objects.get(id=post_id)
    topic = post.topic
    print("Post Owner: " + str(post.owner))
    check_post_owner(request, post)

    if request.method != 'POST':
        # Initial request; pre-fill form with current entry.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:topic', topic_id=topic.id)
    context = {'post': post, 'topic': topic, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

def check_post_owner(request, post):
    """Ensure the topic owner is the same as the currently logged in user."""
    if post.owner != request.user:
        raise Http404
    else:
        return
