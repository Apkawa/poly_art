from django.contrib import admin
from models import News ,Product ,Page, Currency,Section, Manufacturer, TypeProduct, Application

admin.site.register(News)
admin.site.register( Product)
admin.site.register( Page)
admin.site.register( Currency)

class ProductInline( admin.StackedInline ):
    model = Product
    extra = 3

class SectionAdmin(admin.ModelAdmin):
    list_display = [ 'name','slug','type_section','parent','position']
    inlines = [ ProductInline , ]

admin.site.register( Section, SectionAdmin )

admin.site.register( Manufacturer)
admin.site.register( TypeProduct)
admin.site.register( Application)

