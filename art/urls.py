from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^$','poly_art.art.views.main'),
        (r'^news/$','poly_art.art.views.news'),
        (r'^price/$','poly_art.art.views.price'),

        )
