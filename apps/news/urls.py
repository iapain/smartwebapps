from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'apps.news.views.index', name='news-index'),
)
