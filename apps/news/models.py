import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from contrib.feedparser import feedparser

# Create your models here.

class Cluster(models.Model):
    created = models.DateTimeField()
     
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.now()
        super(Cluster, self).save()
  
    def __unicode__(self):
        return u'%d' % self.pk


class NewsSource(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    url = models.URLField(verify_exists=False)
    
    def __unicode__(self):
        return self.name
    
class News(models.Model):
    url = models.URLField(_("URL"), verify_exists=False, unique=True)
    title = models.CharField(_("Title"), max_length=200)
    body = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    source = models.ForeignKey(NewsSource)
    cluster = models.ForeignKey(Cluster, null=True, blank=True)
    
    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    
    def __unicode__(self):
        return self.title
    

@receiver(post_save, sender=NewsSource)
def create_news_items(sender, instance, created, **kwargs):
    """Create a news items from source"""
    #if created:
    feed = feedparser.parse(instance.url)
    for item in feed.entries:
        try:
            news = News.objects.get(url=item.link)
        except News.DoesNotExist:
            if not hasattr(item, 'updated_parsed'):
                date = datetime.datetime.now()
            else:
                date = datetime.datetime(*item.updated_parsed[:6])
            news = News(url=item.link, title=item.title, body=item.summary,
                        date=date, source=instance)
            news.save()
    
