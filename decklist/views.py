from django.shortcuts import render, HttpResponse
from decklist.models import Deck, Card

def deck_list(request):
	decklist = Deck.objects.all()
	context = {'decklist': decklist}
	return render(request, 'decklist.html', context)

def deck(request, deck_id):
	try:
		deck = Deck.objects.get(id = deck_id)
	except Deck.DoesNotExist:
		raise Http404
	context = {'deck' : deck}
	return render(request, 'deck.html', context)

def card_list(request):
	cardlist = Card.objects.all()
	context = {'cardlist' : cardlist}
	return render(request, 'cardlist.html', context)