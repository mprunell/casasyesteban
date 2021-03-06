# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'pages_person', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('short_bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('full_bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Person'])

        # Adding model 'Carousel'
        db.create_table(u'pages_carousel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'pages', ['Carousel'])

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

        # Adding model 'Quote'
        db.create_table(u'pages_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Quote'])

        # Adding model 'Home'
        db.create_table(u'pages_home', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('sub_headline', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('carousel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Carousel'], null=True, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('work', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('footer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Home'])

        # Adding model 'About'
        db.create_table(u'pages_about', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sub_headline', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Quote'])),
        ))
        db.send_create_signal(u'pages', ['About'])

        # Adding model 'Work'
        db.create_table(u'pages_work', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sub_headline', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Quote'])),
        ))
        db.send_create_signal(u'pages', ['Work'])

        # Adding model 'Consultancy'
        db.create_table(u'pages_consultancy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sub_headline', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Quote'])),
        ))
        db.send_create_signal(u'pages', ['Consultancy'])

        # Adding model 'Workshops'
        db.create_table(u'pages_workshops', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sub_headline', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Quote'], null=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Workshops'])

        # Adding model 'Workshop'
        db.create_table(u'pages_workshop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sub_headline', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Quote'], null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Workshops'])),
        ))
        db.send_create_signal(u'pages', ['Workshop'])

        # Adding model 'Contact'
        db.create_table(u'pages_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, blank=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sub_headline', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Quote'], null=True, blank=True)),
        ))
        db.send_create_signal(u'pages', ['Contact'])

        # Adding M2M table for field contacts on 'Contact'
        m2m_table_name = db.shorten_name(u'pages_contact_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'pages.contact'], null=False)),
            ('person', models.ForeignKey(orm[u'pages.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'person_id'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'pages_person')

        # Deleting model 'Carousel'
        db.delete_table(u'pages_carousel')

        # Deleting model 'Image'
        db.delete_table(u'pages_image')

        # Removing M2M table for field carousels on 'Image'
        db.delete_table(db.shorten_name(u'pages_image_carousels'))

        # Deleting model 'Quote'
        db.delete_table(u'pages_quote')

        # Deleting model 'Home'
        db.delete_table(u'pages_home')

        # Deleting model 'About'
        db.delete_table(u'pages_about')

        # Deleting model 'Work'
        db.delete_table(u'pages_work')

        # Deleting model 'Consultancy'
        db.delete_table(u'pages_consultancy')

        # Deleting model 'Workshops'
        db.delete_table(u'pages_workshops')

        # Deleting model 'Workshop'
        db.delete_table(u'pages_workshop')

        # Deleting model 'Contact'
        db.delete_table(u'pages_contact')

        # Removing M2M table for field contacts on 'Contact'
        db.delete_table(db.shorten_name(u'pages_contact_contacts'))


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
            'about': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Carousel']", 'null': 'True', 'blank': 'True'}),
            'footer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sub_headline': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'work': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Workshops']"}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
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