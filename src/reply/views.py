from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from boards.models import Topic
from .forms import PostForm
from django.utils import timezone

# Create your views here.
@login_required
def reply(request, id, post_id):
    form = PostForm()
    topic = get_object_or_404(Topic, board__id = id, id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            topic.last_updated = timezone.now()
            topic.save()
            return redirect('post_topic', pk = id, post_pk = post_id)
    context = {
        'form': form, 
        'topic':topic,
    }
    template = loader.get_template('reply.html')
    return HttpResponse(template.render(context, request))
