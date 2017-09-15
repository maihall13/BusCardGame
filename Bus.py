import CardDeck

#has the dealer deal 10 cards out
def startGame(bus):
    i = 0
    while i < 10:
        i = i + 1
        bus.append(pack.dealCard(deck))
    print ("The dealer lays down 10 cards.\n")

#method that determines if the users guess is higher or lower is correct
def turn(guess):
    if guess == "higher":
        if orders.get(bus[cardplace - 1]) > orders.get(bus[cardplace]):
            print("Congrats the " + bus[cardplace - 1] + " is higher than " + bus[cardplace])
            return True
        else:
            print("Sorry! " + bus[cardplace - 1] + " is lower than " + bus[cardplace])
            return False

    if guess == "lower":
        if orders.get(bus[cardplace - 1]) < orders.get(bus[cardplace]):
            print("Congrats the " + bus[cardplace - 1] + " is lower than " + bus[cardplace])
            return True
        else:
            print("Sorry! " + bus[cardplace - 1] + " is higher than " + bus[cardplace])
            return False

#validation to verify that the user is only typing in the correct information
def askUser():
    while True:
        answer = input("Type in higher or lower to find out \n")
        if answer.lower() not in ("higher","lower"):
            print("You did not enter a valid response")
            continue
        else:
            break
    return turn(answer)


#initiation of game
pack = CardDeck.Deck()
deck = pack.create_deck()
pack.view(deck)

orders = pack.order()
bus = []

startGame(bus)
cardplace = 9
print("The first card is a(n) " + (bus[cardplace]))
print ("Will the next card be higher or lower")

askUser()
result = askUser()
print(result)

#steps
if result == "False":
    print ("game over")
if result == "True":
    print ("Is the next card higher or lower than " + bus[cardplace])
    cardplace = cardplace - 1
    askUser()

