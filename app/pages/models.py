from django.db import models
from django.contrib.auth.models import User
from solo.models import SingletonModel


class Person(User):

    title = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to='photos', blank=True, null=True)
    short_bio = models.TextField(blank=True, null=True)
    full_bio = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Carousel(models.Model):

    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Image(models.Model):

    image = models.ImageField(upload_to='photos')
    carousels = models.ManyToManyField(Carousel, blank=True, null=True)

    def __unicode__(self):
        return self.image.name


class ContentMeta(models.Model):

    slug = models.SlugField()
    title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        abstract = True


class Content(models.Model):

    headline = models.CharField(max_length=256)
    sub_headline = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class Quote(models.Model):

    quote = models.TextField()
    author = models.CharField(max_length=256, blank=True, null=True)

    def __unicode__(self):
        return self.quote[:50] + ' ...'


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


class About(SingletonModel, ContentMeta, Content):

    quote = models.ForeignKey(Quote)

    def __unicode__(self):
        return self.headline

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Work(SingletonModel, ContentMeta, Content):

    quote = models.ForeignKey(Quote)

    def __unicode__(self):
        return self.headline

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Work'


class Consultancy(SingletonModel, ContentMeta, Content):

    quote = models.ForeignKey(Quote)

    def __unicode__(self):
        return self.headline

    class Meta:
        verbose_name = 'Consultancy'
        verbose_name_plural = 'Consultancy'


class Workshops(SingletonModel, ContentMeta, Content):

    quote = models.ForeignKey(Quote, blank=True, null=True)

    def __unicode__(self):
        return u'Workshops'

    def get_workshop_tuples(self):
        tuple_size = 2
        result = []
        workshops = list(self.workshop_set.all())
        while len(workshops) >= tuple_size:
            result.append(tuple(workshops[:tuple_size]))
            workshops = workshops[tuple_size:]
        nones = [None] * (tuple_size - len(workshops))
        result.append(tuple(workshops + nones))
        return result

    class Meta:
        verbose_name = 'Workshops'
        verbose_name_plural = 'Workshops'


class Workshop(ContentMeta, Content):

    name = models.CharField(max_length=256)
    description = models.TextField()
    quote = models.ForeignKey(Quote, blank=True, null=True)
    group = models.ForeignKey(Workshops)


    def __unicode__(self):
        return self.headline[:50]

    class Meta:
        verbose_name = 'Workshop'
        verbose_name_plural = 'Workshop'


class Contact(SingletonModel, ContentMeta, Content):

    quote = models.ForeignKey(Quote, blank=True, null=True)
    contacts = models.ManyToManyField(Person, blank=True, null=True)

    def __unicode__(self):
        return u'Contact'

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
