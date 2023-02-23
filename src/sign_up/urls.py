from .views import sign_up
from django.urls import path

urlpatterns = [
    path('', sign_up, name='sign_up'),
]