from django.test import TestCase
from boards.models import Board, Topic, Post
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class ReplyTopicTestCase(TestCase):
    '''
    Base test case to be used in all `reply_topic` view tests
    '''
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        self.username = 'ayoube'
        self.password = '0000'
        user = User.objects.create_user(username=self.username, email='ayoube@hssi.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=self.topic, created_by=user)
        self.url = reverse('reply', kwargs={'id': self.board.id, 'topic__id': self.topic.id})