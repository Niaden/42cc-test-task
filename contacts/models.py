from django.db import models

# Create your models here.
class Contacts(models.Model):
	class Meta():
		db_table = "contacts"
	contacts_name = models.CharField(max_length = 50)
	contacts_lastname = models.CharField(max_length = 50)
	contacts_birthdate = models.DateField()
	contacts_bio = models.TextField()
	contacts_email = models.EmailField(max_length = 50)
	contacts_jabber = models.EmailField(max_length = 50)
	contacts_skype = models.CharField(max_length = 50)
	contacts_othercontacts = models.TextField()

	def __unicode__(self):
		return "{} - {} {}".format(self.contacts_name, self.contacts_lastname, self.contacts_jabber)