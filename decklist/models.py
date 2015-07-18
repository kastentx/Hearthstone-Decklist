from django.db import models

class Card(models.Model):
# A specific Hearthstone Card 
	name = models.CharField(max_length=100, default="noName")
	
	@classmethod
	def create(cls, name):
		card = cls(name = name)
		return card

class Deck(models.Model):
# A Hearthstone deck containing a bunch of cards 

	def __str__(self):
		return self.name

	name = models.CharField(max_length = 128)
	created = models.DateTimeField(auto_now_add = True)
	description = models.TextField(null = True)
	wins = models.PositiveIntegerField(null = True)
	losses = models.PositiveIntegerField(null = True)
	cards = models.ManyToManyField(Card)
