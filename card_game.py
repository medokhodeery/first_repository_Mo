# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import sys

class Card :
    signs = ['\u2666', '\u2665', '\u2663', '\u2660'] #["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]  
    
    def __init__(self, sign=0, rank=0):
        """Default constructor """
        self.sign = sign
        self.rank = rank
    def __str__(self):
        return (self.ranks[self.rank]+ "of" + self.signs[self.sign])
        """the expression self.ranks[self.rank] means use the attribute rank from the object self
        as an index into the class attribute named ranks and select the appropriate string."""        

class Deck:
    def __init__(self):
        """create the Deck with 52 cards."""
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)
        self.shuffle()
        
    def create_hand(self, card):
        self.cards.append(card)   
    def __len__(self):
        return len(self.cards)   
    def __str__(self):
        """Returns a string representation of the deck."""
        describe_deck = []
        for card in self.cards:
            describe_deck.append(str(card))
        return ', '.join(describe_deck)
    
    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)
        
    def remove(self, i=-1):
        """Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)   
class Hand (Deck):
    def __init__(self, name=""):
       self.cards = []
       self.name = name
       
    def __str__(self):
        return  (self.name + "  " +"hand's is" + "  " +Deck.__str__(self))
    
def game(argv):
    deck = Deck()
    hands = []
    
    for i in range (1,5):
         player =input('insert player %d name \n' %i) 
         if len(argv) > i: 
            player = argv[i]  # get player name from command line parameter
         hands.append(Hand(player))  # add player    
    while len(deck) > 0:
        for hand in hands:
            hand.create_hand(deck.remove())  # remove card from deck and add to hand

    print(hands[0])  # print first player hand
    print(hands[1])   #second player
    print(hands[2])
    print(hands[3])
    
def main(argv=[]):
    answer = "Y"
    while answer.upper() == "Y":
        game(argv)
        answer = input("new hand (Y/N)? : ")
    print("Bye Bye")

        
if __name__ == '__main__':
    main(sys.argv)
       
         
         
         
         
         
         
         
         
         
         
         


