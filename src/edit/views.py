from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from boards.models import Post
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from reply.forms import PostForm

# Create your views here.
@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('post_topic', pk=post.topic.board.id, post_pk=post.topic.id)
