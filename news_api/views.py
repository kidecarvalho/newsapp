from unicodedata import category
from django.http import response
from datetime import datetime
from django.shortcuts import render
from django.template import context
import requests
portugal = "pt"
# Create your views here.

api_key = 'ae7e863a045345e4ab793bbc2537c656'  # kundi_decar@hot...

# GET https://newsapi.org/v2/top-headlines?country=ca&category=business&apiKey=1400ec0372f74deaa50731b608e736d9


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={api_key}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    context = {
        'articles': articles,
        'country_name': country,
        'news_type': category,
        'year': datetime.now().year,
    }

    return render(request, 'news_api/home.html', context)


#url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'
