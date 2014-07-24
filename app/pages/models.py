from django.db import models
from solo.models import SingletonModel


class Carousel(models.Model):

    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Home(SingletonModel):

    headline = models.CharField(max_length=512)
    sub_headline = models.CharField(max_length=1024)
    carousel = models.ForeignKey(Carousel, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    work = models.TextField(blank=True, null=True)
    footer = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'Home'

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'


class Image(models.Model):

    image = models.ImageField(upload_to='photos')
    carousels = models.ManyToManyField(Carousel, blank=True, null=True)

    def __unicode__(self):
        return self.image.name


class Page(models.Model):

    page_title = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    slug = models.CharField(max_length=60)

    def __unicode__(self):
        return self.slug


