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
    TYPE = (
        ('Pr', 'Price'),
        ('Pa', 'Pages'),
    )

    name = models.CharField( max_length = 50)
    slug = models.SlugField(blank=True)
    body_wiki = models.TextField(blank=True)
    body_html = models.TextField(blank=True, editable=False)
    footer_wiki = models.TextField(blank=True)
    footer_html = models.TextField(blank=True, editable=False)
    position = models.IntegerField(default=0)
    parent = models.ForeignKey('self', null=True, blank=True)
    type_section = models.SlugField(max_length=2, choices=TYPE, blank=True)
    def __unicode__(self):
        return self.name
    def save(self):
        self.body_html = make_text(self.body_wiki)
        self.footer_html = make_text(self.footer_wiki)
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
    desc_wiki = models.TextField( max_length=1024, blank=True)
    desc_html = models.TextField( max_length=1024, blank=True, editable=False)
    cell = models.FloatField(default=0)
    currency = models.ForeignKey('Currency', blank=True, null=True)
    #image = models.ImageField(upload_to = '/images/price/')
    image_ext_url = models.URLField(blank=True)
    image_ext_url_thumb = models.URLField(blank=True)
    #section = models.ManyToManyField('Section')
    section = models.ForeignKey('Section')
    manufacturer = models.ForeignKey( 'Manufacturer', null=True, blank=True)
    type_product = models.ForeignKey( 'TypeProduct', null=True, blank=True)
    date_add = models.DateTimeField( auto_now_add=True)
    date_update = models.DateTimeField( auto_now=True, auto_now_add=True)
    def __unicode__(self):
        return self.name
    def save(self):
        self.desc_html = make_text(self.desc_wiki)
        '''
        if self.image_ext_url:
            import uimge
            upl = uimge.Uimge()
            upl.set_host('r_radikal')
            print self.image_ext_url
            upl.upload( str(self.image_ext_url ) )
            self.image_ext_url = upl.img_url
            self.image_ext_url_thumb = upl.img_thumb_url
        '''
        super(Product, self).save()

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


class Application( models.Model):
    '''model for zayavko'''
    name = models.CharField( max_length=512 )
    company = models.CharField( max_length=512, blank=True )
    contact_phone = models.CharField( max_length=45, blank=True )
    email = models.EmailField()
    fields_json= models.TextField()
    fields_human = models.TextField( blank=True )
    datetime_add = models.DateTimeField( auto_now_add= True)

    sending = models.BooleanField( default=False)
    datetime_sending = models.DateTimeField( blank=True, null=True)


