from django.db import models


class Carousel(models.Model):

    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


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


class Home(Page):

    headline = models.CharField(max_length=512)
    sub_headline = models.CharField(max_length=1024)
    carousel = models.ForeignKey(Carousel, blank=True, null=True)
