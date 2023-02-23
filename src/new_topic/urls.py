from django.urls import path
from .views import new_topic

urlpatterns = [
    path('', new_topic, name='new_topic'),
]