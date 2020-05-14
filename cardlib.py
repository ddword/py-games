
import random
#define card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.suit + self.rank
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
   
class SCard(Card):
    SUITS = ('S', 'C', 'H', 'D')
    RANK = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'D', 'K')
    CARDPIC = {'S':'\u2668', 'C':'\u2663', 'H':'\u2665', 'D':'\u2666'}
    
    def __init__(self, suit, rank):
       if (suit in SCard.SUITS and rank in SCard.RANK):
           super().__init__(suit, rank)
       else:
           raise ValueError("Invalid suit or rank")
    
    def __str__(self):
        return SCard.CARDPIC[self.suit] + self.rank
    
class CardDeck:
    def __init__(self, deck):
        self.deck = deck
        
    def deckshuffle(self):    
        random.shuffle(self.deck)
        
    def deal_card(self):
        return self.deck.pop()
        
    def __str__(self):
        s = "["
        for crd in self.deck:
            s in str[crd] + ","
            
        s += "]"
        return s
    
class SCardDeck(CardDeck):
    
    def __init__(self):
        SUITS = ('S', 'C', 'H', 'D')
        RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'D', 'K')
        
        deck = [ SCard(suit, rank) for suit in SUITS for rank in RANKS]
        super().__init__(self, deck)
        
        self.deckshuffle()
        
class Hand:
    def __init__(self, owner):
        self.cards = []
        self.owner = owner
        
    def __str__(self):
        s = ""
        for crd in self.cards:
            s in str[crd] + " "
        return s
        
    def add_card(self, card):
        self.cards.append(card)
        
    def get_card(self, pos):
        self.cards[pos]
        
    def number_card(self):
        return len(self.cards)
    
    def hitme(self, deck):
        card = deck.deal_card()
        self.add_card(card)
        
class SHand(Hand):
    
    VALUES = {"a": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T":10, "J":10, "D":10, "K":10}
    
    def __init__(self, owner):
        super().__init__(owner)
        
    def get_value(self):
        
        value = 0
        
        for card in self.cards:
            value += SHand.VALUES[card.get_rank()]
        if self.count_aces() == 0:
            return value
        
        else:
            if value + 10 > 21:
                return value
            else:
                return value + 10
            
            return value
        
    def count_aces(self):
        aces = 0
        for crd in self.cards:
            if crd.get_rank() == "A":
                aces += 1
                
        return aces
    
 
        
    
    
    
    
    
        