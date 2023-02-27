from .views import UserProfile
from django.urls import path

urlpatterns = [
    path('', UserProfile.as_view(), name='profile'),
]