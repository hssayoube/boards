from django.test import TestCase
from boards.models import Board, Post, Topic
from django.contrib.auth.models import User
from .views import post_topic
from django.urls import reverse, resolve

# Create your tests here.
class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='Django', description='Django board.')
        user = User.objects.create_user(username='ayoube', email='ayoube@hssi.com', password='0000')
        topic = Topic.objects.create(subject='Hello, world', board=board, starter=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=topic, created_by=user)
        url = reverse('post_topic', kwargs={'id': board.id, 'post_id': topic.id})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/board_topics/1/post_topic/1/')
        self.assertEquals(view.func, post_topic)