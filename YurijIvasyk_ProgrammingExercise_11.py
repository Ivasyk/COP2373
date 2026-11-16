import random

class Deck():

    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return self.card_list[self.current_card - 1]

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['clubs', 'diamonds', 'hearts', 'spades']
my_deck = Deck(52)

#deal twelve poker hands, so user can compare before and after shuffling

#created a list to keep cards/variables persistent
hand = []
for i in range(5):
    hand.append(my_deck.deal())

#wrote a function to print users hand to make my life easier
def bleeding():
    for i in range(5):
        d = hand[i]
        r = d % 13
        s = d//13
        print(i + 1, '). ', ranks[r], 'of', suits[s])
    print()

bleeding()

#I don't feel like programming error exceptions
#here's a while loop that forces the user to do what I want
while True:
    mully = input('Do you want to change any of your cards? Y/N ')
    #I hate case-sensitive input
    if mully == 'Y' or mully == 'y':
        trash = input('Which cards would you like to replace? 1-5 ')
        for num in trash.split():
            card = int(num) - 1
            hand[card] = my_deck.deal()
        break
    if mully == 'N' or mully == 'n':
        print('Okay, your hand is still: ')
        bleeding()
        break
    print('please enter a valid response: Y/N ')

bleeding()