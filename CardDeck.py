import random

#card deck creation
class Deck:
    def create_deck(self):
        cardDeck = {"ace": 4, "two": 4, "three": 4, "four": 4,
            "five": 4, "six": 4, "seven": 4, "eight": 4,
            "nine": 4, "ten": 4, "jack": 4, "queen": 4, "king": 4}
        return cardDeck


#deals a random card and removes card from deck
    def dealCard(self, deck):
        #Get random card from dictionary keys
        randomCard = random.choice(list(deck.keys()))
        #print (deck[randomCard])
        while deck[randomCard] == 0:
            randomCard = random.choice(list(deck.keys()))
        deck[randomCard] = deck[randomCard] - 1
        return randomCard

#to show the order of the cards to allow the computer to know which one is higher
    #aces are high in this game
    def order(self):
        orderDeck = {"ace": 13, "two": 1, "three": 2, "four": 3,
            "five": 4, "six": 5, "seven": 6, "eight": 7,
            "nine": 8, "ten": 9, "jack": 10, "queen": 11, "king": 12}
        return orderDeck

#view the deck, for testing mostly
    def view(self, deck):
        for key, value in deck.items():
            print(key, value)