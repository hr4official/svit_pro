"""svit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from appone.views import homepage,contact,help1,product1,login,signup,product2
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',include('appone.urls')),
    path('index.html',include('appone.urls')),
    path('login.html',include('appone.urls')),
    path('help.html',include('appone.urls')),
    path('contact.html',include('appone.urls')),
    path('signup.html',include('appone.urls')),
    path('products5.html',include('appone.urls')),
    path('products.html',include('appone.urls')),
    path('admin/', admin.site.urls),
]
