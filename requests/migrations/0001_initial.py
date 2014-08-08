# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Request'
        db.create_table('Requests', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('request_path', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'requests', ['Request'])


    def backwards(self, orm):
        # Deleting model 'Request'
        db.delete_table('Requests')


    models = {
        u'requests.request': {
            'Meta': {'object_name': 'Request', 'db_table': "'Requests'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_date': ('django.db.models.fields.DateTimeField', [], {}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'request_path': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['requests']