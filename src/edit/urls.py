from django.urls import path
from .views import PostUpdateView

urlpatterns = [
    path('', PostUpdateView.as_view(), name='edit'),
]