"""
URL configuration for DjangoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import RedirectView

from menu.views import home, about, contacts, history, goals, location, phones, moscow, barnaul, news, local_news, global_news, events, upcoming, past, gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/')),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('history/', history, name='history'),
    path('goals/', goals, name='goals'),
    path('location/', location, name='location'),
    path('phones/', phones, name='phones'),
    path('moscow/', moscow, name='moscow'),
    path('barnaul/', barnaul, name='barnaul'),
    path('news/', news, name='news'),
    path('local_news/', local_news, name='local_news'),
    path('global_news/', global_news, name='global_news'),
    path('events/', events, name='events'),
    path('upcoming/', upcoming, name='upcoming'),
    path('past/', past, name='past'),
    path('gallery/', gallery, name='gallery'),
]