from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import News as NewsModel
from .forms import RegistrationForm
from .models import RegistrationData


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


def Register(request):
    context = {
        "form": RegistrationForm
    }

    return render(request, 'signup.html', context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        register = RegistrationData(username = form.cleaned_data['username'],
                                    password = form.cleaned_data['password'],
                                    email = form.cleaned_data['email'],
                                    phone = form.cleaned_data['phone'])
        register.save()

    return redirect('home')
