from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.generic import ListView
from boards.models import Topic, Post

# Create your views here.
class post_topic(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_topic.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        session_key = 'viewed_topic_{}'.format(self.topic.id)
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True
        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('post_pk'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset
