from django.shortcuts import render
from django.views import generic
from scraping.models import News


class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return News.objects.all()
