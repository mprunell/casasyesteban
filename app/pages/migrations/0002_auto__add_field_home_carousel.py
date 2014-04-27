# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Home.carousel'
        db.add_column(u'pages_home', 'carousel',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Carousel'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Home.carousel'
        db.delete_column(u'pages_home', 'carousel_id')


    models = {
        u'pages.carousel': {
            'Meta': {'object_name': 'Carousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'pages.home': {
            'Meta': {'object_name': 'Home', '_ormbases': [u'pages.Page']},
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Carousel']", 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'sub_headline': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'pages.image': {
            'Meta': {'object_name': 'Image'},
            'carousels': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['pages.Carousel']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'pages.page': {
            'Meta': {'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'page_title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['pages']