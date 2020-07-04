from django.urls import path
from .views import News, Home, Contact

urlpatterns = [
    path('news/<int:year>', News, name="news"),
    path('', Home, name="home"),
    path('contact/', Contact, name="contact"),
]
