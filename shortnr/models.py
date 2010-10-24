import base64
import datetime
from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class ShortenedUrl(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    short_url = models.URLField(_('Shortened URL'), verify_exists=False)
    url = models.URLField(_('Regular URL'))
    date_submitted = models.DateTimeField(default=datetime.datetime.now())
    clicks = models.IntegerField(default=0)

    def to_base64(self):
        return base64.urlsafe_b64encode(str(self.id))

    def shorten_url(self):
        self.short_url = settings.SHORTEN_LINK_URL + self.to_base64()
        self.save()
        
    def __unicode__(self):
        return '%s :: %s' % (self.url, self.short_url)
