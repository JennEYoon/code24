import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
# Defines Card object.  

class FrenchDeck:
    # Defines FrenchDeck class.  
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') 
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # Creates all cards in a deck. Initialize deck.     
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

################### JY ####################    
# main, initialzie class, shffle deck    

deck = FrenchDeck() # initialize deck, calls class instance.  
print(deck)
# <__main__.FrenchDeck object at 0x000001E61918A770>  

print(deck[1])  
# Card(rank='3', suit='spades')

print(deck[10]) 
# Card(rank='Q', suit='spades')

print(type(deck[10]))
# <class '__main__.Card'>

# how to draw a card from deck? random choice  
import random  
