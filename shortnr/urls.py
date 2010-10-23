from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^$', 'shortnr.views.shorten_url', name='shorten_url'),
    url(r'^view/(?P<url>\w*\W*)/', 'shortnr.views.view_url', name='view_url'),
)
