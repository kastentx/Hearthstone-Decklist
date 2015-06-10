from django.shortcuts import render, HttpResponse
from decklist.models import Deck

def deck_list(request):
	decklist = Deck.objects.all()
	context = {'decklist': decklist}
	return render(request, 'decklist.html', context)