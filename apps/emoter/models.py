from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.ai.bayes import BayesianClassifier
from contrib.feedparser import feedparser

STATUS_DEFAULT = 'N'
STATUS_POSITIVE = 'H'
STATUS_NEGATIVE = 'S'
STATUS_CHOICES = (
    (STATUS_DEFAULT, _("Neutral")),
    (STATUS_POSITIVE, _("Positive")),
    (STATUS_NEGATIVE, _("Negative"))
)

class SearchTerm(models.Model):
    search = models.CharField(_("Search Term"), max_length=100)

    def __unicode__(self):
        return self.search


class Tweet(models.Model):
    text = models.CharField(_("Message"), max_length=140)
    polarity = models.CharField(_("Polarity"), choices=STATUS_CHOICES, max_length=1, default=STATUS_DEFAULT)
    
    def save(self, *args, **kwargs):
        if not self.id:
            classifier = BayesianClassifier()
            self.polarity = classifier.classify(self.text)
        super(Tweet, self).save()
    
    def __unicode__(self):
        return self.text
    

@receiver(post_save, sender=SearchTerm)
def create_tweets(sender, instance, created, **kwargs):
    """Create a news items from source"""
    #if created:
    classifier = BayesianClassifier()
    url = "feed://search.twitter.com/search.atom?q=" + instance.search
    feed = feedparser.parse(url)
    for item in feed.entries:
        news = Tweet(text=item.summary)
        news.save()
        
