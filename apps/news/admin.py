from django.contrib import admin

from models import Cluster, News, NewsSource

admin.site.register(NewsSource)
admin.site.register(Cluster)
admin.site.register(News)