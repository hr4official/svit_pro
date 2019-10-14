from django.urls import path
from appone.views import homepage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',homepage),
]