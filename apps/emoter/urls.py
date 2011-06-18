from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'apps.emoter.views.index', name='emoter-index'),
)
