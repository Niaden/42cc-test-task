# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contacts.contacts_photo'
        db.add_column('contacts', 'contacts_photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Contacts.contacts_photo'
        db.delete_column('contacts', 'contacts_photo')


    models = {
        u'contacts.contacts': {
            'Meta': {'object_name': 'Contacts', 'db_table': "'contacts'"},
            'contacts_bio': ('django.db.models.fields.TextField', [], {}),
            'contacts_birthdate': ('django.db.models.fields.DateField', [], {}),
            'contacts_email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'contacts_jabber': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'contacts_lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contacts_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contacts_othercontacts': ('django.db.models.fields.TextField', [], {}),
            'contacts_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contacts_skype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['contacts']