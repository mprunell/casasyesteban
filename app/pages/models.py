from django.db import models


class Page(models.Model):

    page_title = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=160)


class Home(Page):

    headline = models.CharField(max_length=512)
    sub_headline = models.CharField(max_length=1024)
