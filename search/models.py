from django.db import models
from django.contrib.postgres.fields import JSONField,ArrayField
from analyte.users.models import User


# Create your models here.
class SearchSocialMedia(models.Model):
        user_id = models.ForeignKey(User, on_delete=models.CASCADE)
        title = models.CharField(max_length=255)
        keywords = models.CharField(max_length=255)
        sites =  ArrayField(models.CharField(max_length=255))
        frequency = models.CharField(max_length=255)
        add_date = models.DateTimeField(auto_now=True)

        def __str__(self):  # __unicode__ on Python 2
            return self.title + " ["  + self.keywords + "]"





class SearchSocialMediaJob(models.Model):
        searchjobs_id = models.ForeignKey(SearchSocialMedia, on_delete=models.CASCADE)
        keywords = models.CharField(max_length=255)
        site = models.CharField(max_length=255)
        last_run = models.DateTimeField(auto_now=True)
        frequency = models.CharField(max_length=254)

class SearchSocialMediaJobResult(models.Model):
        searchsocialmediajob_id = models.ForeignKey(SearchSocialMediaJob, on_delete=models.CASCADE)
        results = JSONField()
        last_run = models.DateTimeField(auto_now=True)


