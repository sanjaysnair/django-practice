from django.urls import path
from .views import News, Home, Contact, Register, addUser

urlpatterns = [
    path('news/<int:year>', News, name="news"),
    path('', Home, name="home"),
    path('contact/', Contact, name="contact"),
    path('signup/', Register, name="register"),
    path('addUser/', addUser, name="addUser"),
]
