from django.conf.urls.defaults import *

urlpatterns = patterns('poly_art.art.views',
        (r'^$','page', {'slug':'zachem-eto-nuzhno'}),
        (r'^news/$','news'),
        (r'^price/([\w-]+)$','price'),
        (r'^page/([\w-]+)$','page'),
        (r'^pages/([\w-]+)$','pages'),
        (r'^app/$','application'),

        )
