from django.db import models

class Card(models.Model):
# A specific Hearthstone Card 

	#def __init__(self, name, cost, playerClass):
	#	self.name = name
	#	self.cost = cost
	#	self.playerClass = playerClass

	def __str__(self):
		return self.name

	#name = models.CharField(max_length=128)
	#cost = models.PositiveIntegerField()
	#playerClass = models.TextField(null = True)

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
