# Licence GPL v3
#Version 1.0

class Player():
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.split_hand = []
        self.split_bet = 0
        self.bet = 0
        self.insurence = 0 
        
    def show_cards(self):
        print(f'\n{self.name} cards:')
        for i in self.cards:
            print (i.name)
        print(f'The current card tally for {self.name} is {self.tally_cards()}')
        print(f'{self.name} s wedger is now {self.bet}\n' )
        
    def get_card(self,card):
        self.cards.append(card)
        
    def place_bet(self):
        self.bet += int(input(f'{self.name}, place your bet(10/20/50/100/1000)\n'))
        print(f'{self.name} s wedger is now {self.bet}\n' )
        
    def double_down(self, card):
        self.get_card(card)
        self.bet *= 2
        print (f'{self.name} s wedger is now {self.bet}\n')
        
    def insure(self):
        self.insurance = self.bet*0.5
        print(f'An insurance of {self.insurance} added\n')  
        
    def split(self):
        self.split_hand = self.cards.pop()
        self.split_bet = self.bet
        
    def surrender(self):
        #del(self)
        pass
        
    def hit(self,card):
        self.get_card(card)
        
    def tally_cards(self):
        self.tally = 0
        for i in self.cards:
            self.tally += int(i)
        for i in self.cards:
            if int(i) == 11:
                if self.tally > 21:
                    self.tally -= 10
        return self.tally

class Card():
    def __init__(self,name):
        self.name = name
    def __int__(self):
        if 'J' in self.name or 'K' in self.name or 'Q' in self.name or  '10' in self.name:
            return 10
        for i in range(10):
            if str (i) in self.name:
                return i
        if 'A' in self.name:
            return 11
    def __str__(self):
        return self.name
#defime end of the game
def end_game():
    for i in players:
        if i.tally_cards()<house.tally_cards():
            pass
#create a list of player names
players = []
while True:
    players_num = int(input('Enter number of players(1-5)'))
    if 0 < players_num <= 5:
        print(f'We have {players_num} players')
        break
    else:
        #clear_output()
        print('Invalid nuber of players! Please try again.')
        
for i in range(players_num):
    players.append ('player_' + str(i))
print(players) 

#replace the list of player names with a list of player objects with the names from list of player names assigned
for i in range(len(players)):
    players[i] = Player( players[i])
#print(players)

#create the cards
types = ['2','3','4','5','6','7','8','9','10','A','J','Q']
group = ['diamonds','spades','clubs','hearts' ]
all_cards = []
card = ''
for i in group:
    for j in types:
        card = j+'_'+i
        all_cards.append(card)
#print(all_cards)
for i in range(len(all_cards)):
    all_cards[i] = Card(all_cards[i])
#print(all_cards[5])

#shuffle the cards
import random
shuffled_cards = random.shuffle(all_cards)

#let players place bets in turn
for i in players:
    #i.show_cards()
    i.place_bet()

#deal the cards
for i in range(2):
    for i in (players):
          i.get_card(all_cards.pop())
for i in players:
    i.show_cards()
house = Player('house')
house.get_card(all_cards.pop())
house.show_cards()
    
#let players take options
for i in players:
    i.show_cards()
    while True:
            selection = (str(input(f'{i.name}, do you want to take a hit (H), stand(T), double-down(D), splitt(S), insure(I) or surrender(R) ?').upper()))
            if selection  == 'T':
                i.show_cards()
                break
            elif selection == 'H':
                i.hit(all_cards.pop())
                i.show_cards()
                break
            elif selection == 'D':
                i.double_down(all_cards.pop())
                i.show_cards()
                break
            elif selection == 'S':
                i.split()
                i.show_cards()
                break
            elif selection =='I':
                i.insure()
                i.show_cards()
                break
            elif selection == 'S':
                i.surrender()
                i.show_cards()
                break
            else:
                print('Sorry {self.name}, your selection is invalid. Try again.')
                continue

if house.tally_cards()<17:
    house.get_card(all_cards.pop())
    house.show_cards()
if house.tally_cards()<17:
    house.get_card(all_cards.pop())
    house.show_cards()
if house.tally_cards()<17:
    house.get_card(all_cards.pop())
    house.show_cards()
 
