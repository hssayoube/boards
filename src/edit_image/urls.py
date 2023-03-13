from django.urls import path
from .views import image_editor

urlpatterns = [
    path('Image-Editor/', image_editor, name='image_editor'),
]