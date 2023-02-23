from django.urls import path
from .views import reply

urlpatterns = [
    path('', reply, name='reply')
]