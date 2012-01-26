from django.db import models
from taggit.managers import TaggableManager

class Record(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=255, null=True, blank=True)
    body=models.TextField(max_length=1000, null=True, blank=True)
    tags = TaggableManager()
    def __unicode__(self):
        return self.title
