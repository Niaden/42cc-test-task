# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contacts'
        db.create_table('contacts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contacts_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contacts_lastname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contacts_birthdate', self.gf('django.db.models.fields.DateField')()),
            ('contacts_bio', self.gf('django.db.models.fields.TextField')()),
            ('contacts_email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('contacts_jabber', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('contacts_skype', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contacts_othercontacts', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['Contacts'])


    def backwards(self, orm):
        # Deleting model 'Contacts'
        db.delete_table('contacts')


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
            'contacts_skype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['contacts']