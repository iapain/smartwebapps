from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from apps.djangoratings.fields import RatingField

# Create your models here.

class Movie(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    
    def __unicode__(self):
        return self.title
    
class MovieRating(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    rating = RatingField(range=5)
    
    def __unicode__(self):
        return "%s rated %s" % (self.user.username, self.movie.title)


    
