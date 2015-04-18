from django.db import models

class Cards(models.Model):
	key = models.CharField(max_length=250)
	info = models.CharField(max_length=5000)
	index = models.IntegerField()

class Flashcards(models.Model):
	title = models.CharField(max_length=200)
	vocabulary = models.ForeignKey(Cards)
	total_cards = models.IntegerField()
	post_date = models.DateTimeField('date posted')
	url = models.CharField(max_length=32)

