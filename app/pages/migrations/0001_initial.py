# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carousel'
        db.create_table(u'pages_carousel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'pages', ['Carousel'])

        # Adding model 'Home'
        db.create_table(u'pages_home', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('sub_headline', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('carousel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Carousel'], null=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Home'])

        # Adding model 'Image'
        db.create_table(u'pages_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'pages', ['Image'])

        # Adding M2M table for field carousels on 'Image'
        m2m_table_name = db.shorten_name(u'pages_image_carousels')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('image', models.ForeignKey(orm[u'pages.image'], null=False)),
            ('carousel', models.ForeignKey(orm[u'pages.carousel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['image_id', 'carousel_id'])

        # Adding model 'Page'
        db.create_table(u'pages_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'pages', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Carousel'
        db.delete_table(u'pages_carousel')

        # Deleting model 'Home'
        db.delete_table(u'pages_home')

        # Deleting model 'Image'
        db.delete_table(u'pages_image')

        # Removing M2M table for field carousels on 'Image'
        db.delete_table(db.shorten_name(u'pages_image_carousels'))

        # Deleting model 'Page'
        db.delete_table(u'pages_page')


    models = {
        u'pages.carousel': {
            'Meta': {'object_name': 'Carousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'pages.home': {
            'Meta': {'object_name': 'Home'},
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Carousel']", 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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