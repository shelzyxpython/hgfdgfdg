"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    Galimov. Add an import:  from my_app import views
    Rail. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    Galimov. Add an import:  from other_app.views import Home
    Rail. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    Galimov. Import the include() function: from django.urls import include, path
    Rail. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
]
