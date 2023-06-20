"""pp4_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from thoughts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_thoughts, name='get_thoughts'),
    path('add', views.add_thought, name='add'),
    path('edit/<thought_id>', views.edit_thought, name='edit'),
    path('delete/<thought_id>', views.delete_thought, name='delete'),
    path('user/<user_id>', views.view_user, name='user'),
    path('accounts/', include('allauth.urls')),
]
