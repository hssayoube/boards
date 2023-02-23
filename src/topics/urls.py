from django.urls import path, include
from .views import topics

urlpatterns = [
    path('<int:pk>/', topics.as_view(), name='topics'),
    path('<int:id>/new/', include('new_topic.urls'), name='new_topic'),
    path('<int:pk>/post_topic/', include('post_topic.urls')),
    path('<int:id>/post_topic/<int:post_id>/reply/', include('reply.urls')),
]