from django.db import models

# Create your models here.
class Cards(models.Model):
	title = models.CharField(max_length=200)
	vocabulary = models.CharField()
	post_date = models.DateTimeField('date posted')
