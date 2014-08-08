from django.db import models
from django.http.request import HttpRequest
import datetime

# Create your models here.
class Request(models.Model):
	class Meta():
		db_table = "Requests"
	request_date = models.DateTimeField()
	request_method = models.CharField(max_length = 50)
	request_path = models.CharField(max_length = 300)

	def __unicode__(self):
		return "{} {} {}".format(self.request_date,self.request_path,self.request_method)
