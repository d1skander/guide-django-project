"""
URL configuration for guide_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main_page, name='main'),
    path('sight/<uuid:id>/', views.sight_page, name='sight'),
    path('reg/', views.reg_page, name='reg'),
    path('auth/', views.auth_page, name='auth'),
    path('info/', views.info_page, name='info'),
    path('del_profile/', views.delete_user, name='del_profile'),
    path('profile/', views.profile_page, name='profile'),
    path('edit_email/', views.edit_email, name='edit_email'),
    path('edit_password', views.edit_password, name='edit_password'),
    path('edit_username', views.edit_username, name='edit_username'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)