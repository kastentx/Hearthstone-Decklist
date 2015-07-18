import os
import codecs
import json
from decklist.models import Card

def buildList():

    cardPack = []

    fileObj = codecs.open(os.path.join('data',
                                       'AllSets.json'), 'r', encoding='utf-8')
    jsonData = json.loads(fileObj.read())
        
    for collection in jsonData:                                                         # loops through all the different card sets
        for card in jsonData[collection]:

            if card['name'] not in cardPack:
                newCard = Card.create(card['name'])
                #newCard = Card(**card)                                                     # create by passing dict
                newCard.save()
                cardPack.append(card['name'])

            #if 'cost' in card:                                                          # checks to ensure card is playable
                
                #if ('playerClass' in card):                                             # checks for class specific vs general cards
                    #playerClass = card['playerClass']
                #else:
                    #playerClass = 'All Classes'

                #if card['name'] not in cardPack:                                        # adds uniquely named cards to cardPack

                    #cardPack.append(Card(card['name'], str(card['cost']), playerClass, card['type']))


    #for card in cardPack:                                                               # displays that list of cards in cardPack
        #if card.playerClass == 'Rogue':
            #print ('Card: ' + card.name + ' ' + card.cost + ' ' + card.cardType + '\n')
