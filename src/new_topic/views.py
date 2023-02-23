from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from boards.models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def new_topic(request, id):
    board = get_object_or_404(Board, id = id)
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()

            Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = request.user,
            )

            return redirect('post_topic', pk = id, post_pk = topic.id)
    else:
        form = NewTopicForm()

    template = loader.get_template('new_topic.html')
    context = {
        'board':board,
        'form':form,
    }
    return HttpResponse(template.render(context, request))