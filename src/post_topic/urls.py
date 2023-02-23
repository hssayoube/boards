from django.urls import path, include
from .views import post_topic

urlpatterns = [
    path('<int:post_pk>/', post_topic.as_view(), name='post_topic'),
    path('<int:post_id>/edit', include('edit.urls')),
]