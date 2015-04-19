from django.db import models

class Cards(models.Model):
	Key = models.CharField(max_length=250)
	Info = models.CharField(max_length=5000)

	def _unicode_(self):
		return self.Key

class Flashcards(models.Model):
	Title = models.CharField(max_length=200)
	Vocabulary = models.ForeignKey(Cards)
	Url = models.CharField(max_length=32)

	def _unicode_(self):
		return self.Title

