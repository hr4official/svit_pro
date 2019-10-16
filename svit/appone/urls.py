from django.urls import path
from appone.views import homepage,contact,help1,product1,login,signup,product2
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',homepage),
    path('contact.html',contact),
    path('help.html',help1),
    path('products.html',product1),
    path('login.html',login),
    path('signup.html',signup),
    path('products5.html',product2),
]