from django.contrib import admin

from models import Cluster, News, NewsSource

admin.site.register(NewsSource, Cluster, News)