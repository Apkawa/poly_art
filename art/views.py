# Create your views here.
from django.shortcuts import render_to_response
from models import News, Product, Section, Manufacturer, Page

def main( request):
    return render_to_response('art/main.html')

def news(request):
    news = News.objects.all().order_by('-date_add')[:5]
    return render_to_response('art/news.html',{'news':news})

def price( request, slug):
    section = Section.objects.get(slug = slug )
    products = Product.objects.filter( section = section )
    manufs = Manufacturer.objects.filter( product__section = section).distinct()
    
    return render_to_response('art/price.html', {'products': products, 'section':section, 'manufs':manufs})

def page( request, slug):
    page = Page.objects.get( slug = slug)
    return render_to_response('art/page.html', {'page':page})



