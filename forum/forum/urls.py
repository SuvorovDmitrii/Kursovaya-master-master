"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mysite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', views.register, name='registration'),
    path('request_create', views.requestUser, name='request_create'),
    path('user_room_admin', views.SectionViewAdmin.as_view(), name='user_room_admin'),
    path('my_order', views.SectionView.get, name='my_order'),
    path('my_order/delete/<int:id>', views.SectionView.remove, name='remove_order'),
    path('my_order/edit', views.edit_profile, name='edit_profile'),
    path('password/', views.change_password, name='password'),
    path('', views.index, name='main'),
    path('stat', views.getStatistic, name='stat'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)