from django.contrib import admin
from models import News ,Product ,Page, Currency,Section, Manufacturer, TypeProduct

admin.site.register(News)
admin.site.register( Product)
admin.site.register( Page)
admin.site.register( Currency)

class SectionAdmin(admin.ModelAdmin):
    list_display = [ 'name','parent','position']
admin.site.register( Section, SectionAdmin )
admin.site.register( Manufacturer)
admin.site.register( TypeProduct)

