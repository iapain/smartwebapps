from django.db import models
from django.utils.translation import ugettext_lazy as _

STATUS_DEFAULT = 1
STATUS_POSITIVE = 2
STATUS_NEGATIVE = 3
STATUS_CHOICES = (
    (STATUS_DEFAULT, _("Neutral")),
    (STATUS_POSITIVE, _("Positive")),
    (STATUS_NEGATIVE, _("Negative"))
)

class Tweet(models.Model):
    text = models.CharField(_("Message"), max_length=140)
    polarity = models.CharField(_("Polarity"), choices=STATUS_CHOICES, max_length=1, default=STATUS_DEFAULT)
    
    def __unicode__(self):
        return self.text
    
