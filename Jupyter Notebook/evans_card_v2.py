import random

class Card:
    _rank_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, r = "None", s = "None"):
        self._rank = r
        self._suit = s
        
    def display(self):
        print(self._rank, "of", self._suit)

    def beats(self, other):
        order = Card._rank_order
        try:
            pos_self = order.index(self._rank)
            pos_other = order.index(other._rank)
            return pos_self > pos_other
        except:
            raise BreakEvansCode("WHY MUST YOU BREAK MY CODE")
                                 

class Deck:
    _ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    _suits = ["Hearts", "Clubs", "Diamonds", "Spades"]

    def __init__(self):
        self._cards_left = 52
        self._drawn = {}
        for r in Deck._ranks:
            for s in Deck._suits:
                self._drawn[Card(r,s)] = False 
        
    def draw(self):
        if self._cards_left > 0:
            self._cards_left -= 1
            card = random.choice(list(self._drawn))
            while self._drawn[card]:
                card = random.choice(list(self._drawn))
            self._drawn[card] = True        
            return card
        else:
            raise BreakEvansCode("WANTED TO SEE WHAT WOULD HAPPEN, DID YOU?")
    
class BreakEvansCode(Exception):
    pass
        
