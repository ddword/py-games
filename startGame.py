from cardlib import *

deck01 = SCardDeck()
player1 = input("Enter your name player 1:")
player2 = input("Enter your name player 2 :")

hand1 = SHand(player1)
hand2 = SHand(player2)

for i in range(3):
    hand1.hitme(deck01)
    hand2.hitme(deck01)
    
print()
print("Here your hands: ")
print("------")
print("{} Hand: {}".format(hand1.owner, hand1))
print("{} Hand: {}".format(hand2.owner, hand2))
print()

if hand1.get_value() > hand2.get_value():
    print("The winner is : {}".format(hand1.owner))
elif hand2.get_value() > hand1.get_value():
    print("The winner is : {}".format(hand2.owner))
else:
    print("It is a ied game!!!")