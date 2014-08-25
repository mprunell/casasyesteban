# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Home.footer'
        db.delete_column(u'pages_home', 'footer')

        # Deleting field 'Home.headline'
        db.delete_column(u'pages_home', 'headline')

        # Deleting field 'Home.sub_headline'
        db.delete_column(u'pages_home', 'sub_headline')

        # Adding field 'Home.quote'
        db.add_column(u'pages_home', 'quote',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Quote'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Home.consultancy'
        db.add_column(u'pages_home', 'consultancy',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Consultancy'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Home.workshops'
        db.add_column(u'pages_home', 'workshops',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Workshops'], null=True, blank=True),
                      keep_default=False)


        # Renaming column for 'Home.about' to match new field type.
        db.rename_column(u'pages_home', 'about', 'about_id')
        # Changing field 'Home.about'
        db.alter_column(u'pages_home', 'about_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.About'], null=True))
        # Adding index on 'Home', fields ['about']
        db.create_index(u'pages_home', ['about_id'])


        # Renaming column for 'Home.work' to match new field type.
        db.rename_column(u'pages_home', 'work', 'work_id')
        # Changing field 'Home.work'
        db.alter_column(u'pages_home', 'work_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Work'], null=True))
        # Adding index on 'Home', fields ['work']
        db.create_index(u'pages_home', ['work_id'])


    def backwards(self, orm):
        # Removing index on 'Home', fields ['work']
        db.delete_index(u'pages_home', ['work_id'])

        # Removing index on 'Home', fields ['about']
        db.delete_index(u'pages_home', ['about_id'])

        # Adding field 'Home.footer'
        db.add_column(u'pages_home', 'footer',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Home.headline'
        db.add_column(u'pages_home', 'headline',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=512),
                      keep_default=False)

        # Adding field 'Home.sub_headline'
        db.add_column(u'pages_home', 'sub_headline',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=1024),
                      keep_default=False)

        # Deleting field 'Home.quote'
        db.delete_column(u'pages_home', 'quote_id')

        # Deleting field 'Home.consultancy'
        db.delete_column(u'pages_home', 'consultancy_id')

        # Deleting field 'Home.workshops'
        db.delete_column(u'pages_home', 'workshops_id')


        # Renaming column for 'Home.about' to match new field type.
        db.rename_column(u'pages_home', 'about_id', 'about')
        # Changing field 'Home.about'
        db.alter_column(u'pages_home', 'about', self.gf('django.db.models.fields.TextField')(null=True))

        # Renaming column for 'Home.work' to match new field type.
        db.rename_column(u'pages_home', 'work_id', 'work')
        # Changing field 'Home.work'
        db.alter_column(u'pages_home', 'work', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pages.about': {
            'Meta': {'object_name': 'About'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Quote']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sub_headline': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'pages.carousel': {
            'Meta': {'object_name': 'Carousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'pages.consultancy': {
            'Meta': {'object_name': 'Consultancy'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Quote']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sub_headline': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'pages.contact': {
            'Meta': {'object_name': 'Contact'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['pages.Person']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Quote']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sub_headline': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'pages.home': {
            'Meta': {'object_name': 'Home'},
            'about': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.About']", 'null': 'True', 'blank': 'True'}),
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Carousel']", 'null': 'True', 'blank': 'True'}),
            'consultancy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Consultancy']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Quote']", 'null': 'True', 'blank': 'True'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Work']", 'null': 'True', 'blank': 'True'}),
            'workshops': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Workshops']", 'null': 'True', 'blank': 'True'})
        },
        u'pages.image': {
            'Meta': {'object_name': 'Image'},
            'carousels': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['pages.Carousel']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'pages.person': {
            'Meta': {'object_name': 'Person', '_ormbases': [u'auth.User']},
            'full_bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'short_bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'pages.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote': ('django.db.models.fields.TextField', [], {})
        },
        u'pages.work': {
            'Meta': {'object_name': 'Work'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Quote']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sub_headline': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'pages.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Workshops']"}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Quote']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sub_headline': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'pages.workshops': {
            'Meta': {'object_name': 'Workshops'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Quote']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sub_headline': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pages']