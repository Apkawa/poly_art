# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound, Http404
from models import News, Product, Section, Manufacturer, Page, Application

def main( request):
    return render_to_response('art/main.html')

def news(request):
    news = News.objects.all().order_by('-date_add')[:5]
    return render_to_response('art/news.html',{'news':news})

def price( request, slug=None):
    if slug:
        try:
            section = Section.objects.get(slug = slug )
        except Section.DoesNotExist:
            raise Http404
        products = Product.objects.filter( section = section )
        manufs = Manufacturer.objects.filter( product__section = section).distinct()
    return render_to_response('art/price.html', {'products': products, 'section':section, 'manufs':manufs})

def page( request, slug):
    page = Page.objects.get( slug = slug)
    return render_to_response('art/page.html', {'page':page})

from django import forms


class ApplicForm(forms.ModelForm):
    text = forms.CharField( widget=forms.Textarea)

    class Meta:
        model = Application
        fields = ( 'name', 'company', 'contact_phone','email')

def application( request):
    a_form = ApplicForm()
    return render_to_response('art/appl.html', {'form': a_form})

