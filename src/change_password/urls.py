from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path('', views.PasswordChangeView.as_view(template_name='password_change.html'), name='change_password'),
    path('password_change_done/', views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]