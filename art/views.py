# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound, Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
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
        #manufs = Manufacturer.objects.filter( product__section = section).distinct()
        #products = []
        #if manufs:
        #    for manuf in manufs:
        #        products.append( [ manuf, Product.objects.filter( section=section, manufacturer = manuf) ] )
        #products.append( [ None, Product.objects.filter( section=section, manufacturer = None) ] )
        #print products
        return render_to_response('art/price.html', {'products': products, 'section':section, })#'manufs':manufs})

def page( request, slug):
    page = Page.objects.get( slug = slug)
    return render_to_response('art/page.html', {'page':page})


def pages( request, slug ):
    try:
        section = Section.objects.get(slug = slug, type_section = 'Pa' )
    except Section.DoesNotExist:
        raise Http404
    pages = Page.objects.filter( section = section )
    return render_to_response('art/pages_in_section.html' , {'pages':pages, 'section':section})


from django import forms
class ApplicForm(forms.ModelForm):
    text = forms.CharField( widget=forms.Textarea)

    class Meta:
        model = Application
        fields = ( 'name', 'company', 'contact_phone','email')

def application( request):
    if request.method == 'POST':
        a_form = ApplicForm( request.POST)
        print request.POST
        if a_form.is_valid():
            name = a_form.cleaned_data['name']
            company = a_form.cleaned_data['company']
            contact_phone = a_form.cleaned_data['contact_phone']
            email = a_form.cleaned_data['email']
            text = a_form.cleaned_data['text']
            import json
            fields_json = json.dumps( {'text':text} )
            
            app, created = Application.objects.get_or_create( name=name, company=company, contact_phone=contact_phone, email=email, fields_json = fields_json )
            if created:
                print 'created'
                #send email
                return HttpResponseRedirect( reverse( 'poly_art.art.views.page', args=('spasibo-za-zayavku',) ) )

            else: 
                return HttpResponseRedirect( reverse( 'poly_art.art.views.application' ))


    else:
        a_form = ApplicForm()
    return render_to_response('art/appl.html', {'form': a_form})

