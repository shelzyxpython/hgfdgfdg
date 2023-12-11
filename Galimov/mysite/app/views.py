from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contacts(request):
    contact = {'list': ['Sim: 880555300000', 'Telegram: @sh3lzyx']}
    return render(request, "contacts.html", contact)
