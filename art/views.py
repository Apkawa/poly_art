# Create your views here.
from django.shortcuts import render_to_response
from models import News

def main( request):
    return render_to_response('art/main.html')

def news(request):
    news = News.objects.all().order_by('-date_add')[:5]
    return render_to_response('art/news.html',{'news':news})

def price( request):
    return render_to_response('art/price.html')

