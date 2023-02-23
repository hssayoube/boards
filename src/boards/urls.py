from .views import BoardListView
from django.urls import path

urlpatterns = [
    path('', BoardListView.as_view(), name='home'),
]