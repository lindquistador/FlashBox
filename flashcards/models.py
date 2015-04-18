from django.db import models

# Create your models here.
class flashcard(models.Model):
	title = models.CharField(max_length=200)
	vocabulary = models.CharField(max_length=10000)
	post_date = models.DateTimeField('date posted')
	url = models.CharField(max_length=32)
