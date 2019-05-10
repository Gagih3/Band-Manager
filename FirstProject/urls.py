"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .views import Main, SignUp, Logout, Login, ProfileView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main/', Main.as_view(), name='main'),
    path('main/sign_up', SignUp.as_view(), name='sign_up'),
    path('main/logout', Logout.as_view(), name='logout'),
    path('main/login', Login.as_view(), name='login'),
    path('main/profile', ProfileView.as_view(), name='profile')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
