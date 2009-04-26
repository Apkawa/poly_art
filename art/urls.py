from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^$','poly_art.art.views.main'),
        (r'^news/$','poly_art.art.views.news'),
        (r'^price/([\w-]+)$','poly_art.art.views.price'),
        (r'^page/([\w-]+)$','poly_art.art.views.page'),

        )
