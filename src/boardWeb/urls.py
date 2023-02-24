"""boardWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('', include('boards.urls')),
    path('admin/', admin.site.urls),
    path('board_topics/', include('topics.urls')),
    path('sign_up/', include('sign_up.urls')),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', include('login.urls')),
    path('reset/', include('password_reset.urls')),
    path('change_password/', include('change_password.urls')),
    path('profile/', include('account_profile.urls')),
    path('tinymce/', include('tinymce.urls')),
]
