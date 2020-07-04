from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import News as NewsModel


def Home(request):
    news = NewsModel.objects.all()
    context = {
        "header_title": "Sanjay's blog",
        "news": news
    }
    return render(request, 'home.html', context)


def News(request, year=2020):
    news_list = NewsModel.objects.filter(pub_date__year=year)
    context = {
        "lang_list": ["Python", "Java", "PHP", "React Native"],
        "year": year,
        "news_list": news_list
    }
    return render(request, 'news.html', context)


def Contact(request):
    return render(request, 'contact.html')
