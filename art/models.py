from django.db import models

def wiki2html(text):
    from creoleparser import text2html
    return text2html( text, method='xhtml' )
def typograf(text):
    from typographus import typographus
    return typographus.typo( text )

def make_text(text):
    text = wiki2html( text ) 
    #text = typograf(text)
    return text 

def title2slug(text):
    import pytils
    return pytils.translit.slugify(text)

class Section(models.Model):
    name = models.CharField( max_length = 50)
    slug = models.SlugField(blank=True)
    body_wiki = models.TextField(blank=True)
    body_html = models.TextField(blank=True, editable=False)
    position = models.IntegerField(default=0)
    parent = models.ForeignKey('self', null=True, blank=True)
    def __unicode__(self):
        return self.name
    def save(self):
        self.body_html = make_text(self.body_wiki)
        self.slug = title2slug( self.name)
        super(Section, self).save()



class Page(models.Model):
    title = models.CharField( max_length=140)
    slug = models.SlugField(blank=True)
    body_wiki = models.TextField()
    body_html = models.TextField(blank=True)
    section = models.ForeignKey('Section', null=True, blank=True)
    date_add = models.DateTimeField( auto_now_add=True)
    date_update = models.DateTimeField( auto_now=True, auto_now_add=True)
    def __unicode__(self):
        return self.title
    def save(self):
        self.body_html = make_text(self.body_wiki)
        self.slug = title2slug( self.title[:45])
        super(Page, self).save()

class News(models.Model):
    title = models.CharField( max_length=140)
    slug = models.SlugField(blank=True, editable=False)
    body_wiki = models.TextField()
    body_html = models.TextField(blank=True, editable=False)
    date_add = models.DateTimeField( auto_now_add=True)
    def __unicode__(self):
        return self.title
    def save(self):
        self.body_html = make_text(self.body_wiki)
        self.slug = title2slug( self.title)
        super(News, self).save()

class Product(models.Model):
    name = models.CharField( max_length=256)
    desc = models.TextField( max_length=1024)
    cell = models.FloatField(default=0)
    currency = models.ForeignKey('Currency')
    #image = models.ImageField(upload_to = '/images/price/')
    image_ext_url = models.URLField(blank=True)
    image_ext_url_thumb = models.URLField(blank=True)
    section = models.ManyToManyField('Section')
    manufacturer = models.ForeignKey( 'Manufacturer', null=True, blank=True)
    type_product = models.ForeignKey( 'TypeProduct', null=True, blank=True)
    date_add = models.DateTimeField( auto_now_add=True)
    date_update = models.DateTimeField( auto_now=True, auto_now_add=True)
    def __unicode__(self):
        return self.name

class Currency( models.Model):
    "This valutas"
    name = models.CharField( max_length=10)
    display = models.CharField( max_length=5)
    def __unicode__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField( max_length = 50)
    slug = models.SlugField(blank=True)
    body_wiki = models.TextField(blank=True)
    body_html = models.TextField(blank=True)
    position = models.IntegerField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    def __unicode__(self):
        return self.name
    def save(self):
        self.body_html = make_text(self.body_wiki)
        self.slug = title2slug( self.name)
        super(Manufacturer, self).save()

class TypeProduct(models.Model):
    name = models.CharField( max_length = 50)
    slug = models.SlugField(blank=True)
    body_wiki = models.TextField()
    body_html = models.TextField()
    image_ext_url = models.URLField(blank=True)
    image_ext_url_thumb = models.URLField(blank=True)
    position = models.IntegerField(default=0)
    parent = models.ForeignKey('self', null=True, blank=True)
    def __unicode__(self):
        return self.name
    def save(self):
        self.body_html = make_text(self.body_wiki)
        self.slug = title2slug( self.name)
        super(TypeProduct, self).save()
# Create your models here.
