from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def history(request):
    return render(request, 'history.html')


def goals(request):
    return render(request, 'goals.html')


def location(request):
    return render(request, 'location.html')


def phones(request):
    return render(request, 'phones.html')


def moscow(request):
    return render(request, 'moscow.html')


def barnaul(request):
    return render(request, 'barnaul.html')


def news(request):
    return render(request, 'news.html')


def local_news(request):
    return render(request, 'local_news.html')


def global_news(request):
    return render(request, 'global_news.html')


def events(request):
    return render(request, 'events.html')


def upcoming(request):
    return render(request, 'upcoming.html')


def past(request):
    return render(request, 'past.html')


def gallery(request):
    return render(request, 'gallery.html')