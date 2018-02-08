# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = True
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        res = "Hand contains"
        for c in self.hand:
            res = res+" "+ c.__str__()
        return res
    
    def add_card(self, card):
        self.hand.append(Card(random.choice(SUITS),random.choice(RANKS)))

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        val = 0
        ranks = []
        for i in range(len(self.hand)):
            ranks.append(self.hand[i].get_rank())
        if 'A' not in ranks:
            for c in self.hand:
                val+=VALUES[c.get_rank()]
        else:
            for c in self.hand:
                val+=VALUES[c.get_rank()]
            if val+10 <= 21:
                val += 10
        return val
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck =[]
        for i in range(13):
            r = RANKS[i]
            for j in range(4):
                s = SUITS[j]
                self.deck.append(Card(s,r))
                

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        dc = random.choice(self.deck)
        self.deck.remove(dc)
        return dc
    
    def __str__(self):
        res = "Deck contains"
        for c in self.deck:
            res = res+" "+ c.__str__()
        return res 


#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, deck, score
    outcome = ""
    #score = 0
    deck = Deck()
    deck.shuffle()
    dealer = Hand()
    player = Hand()
    p1 = deck.deal_card()
    p2 = deck.deal_card()
    player.add_card(p1)
    player.add_card(p2)
    d1 = deck.deal_card()
    d2 = deck.deal_card()
    dealer.add_card(d1)
    dealer.add_card(d2)
    #print "player's hand:"+player.__str__()
    #print "dealer's hand:"+dealer.__str__()
    in_play = True

def hit():
    global player, in_play, score, outcome
    if player.get_value()<=21:
        p = deck.deal_card()
        player.add_card(p)
        if player.get_value()>21:
            in_play = False
            outcome = "You are busted!You lose!"
            score -= 1
        #print "player's hand:"+player.__str__()
    
        #print "You'are busted!"
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global player, dealer, in_play, outcome, score
    if player.get_value()>21:
        print "Player is busted Dealer wins!"
        score += 1
        in_play = False
    while dealer.get_value()<17:
        d = deck.deal_card()
        dealer.add_card(d)
    if dealer.get_value()>21:
        outcome = "Dealer is busted!You win!"
        score += 1
        in_play = False
    else:
        if player.get_value()>dealer.get_value():           
            outcome = "You win!"
            score += 1
            in_play = False
        else:            
            outcome = "You lose!"
            score -= 1
            in_play = False
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    global player, dealer, in_play,outcome
    canvas.draw_text("Blackjack",[100,100],50,"#42ebf4")
    canvas.draw_text("Dealer",[80,200],30,"Black")
    canvas.draw_text("Player",[80,400],30,"Black")
    canvas.draw_text(outcome,[250,200],30,"Black")
    canvas.draw_text("Score "+str(score),[400,100],30,"Black")
    if in_play == True:
        canvas.draw_text("Hit or Stand?",[250,400],30,"Black")
    else:
        canvas.draw_text("New deal?",[250,400],30,"Black")
        
    for p in player.hand:
        i = player.hand.index(p)
        if i<5:
            pos = [80+100*i,420]
            p.draw(canvas,pos)
    for d in dealer.hand:
        i = dealer.hand.index(d)
        pos = [80+100*i,220]
        if i == 0:
            if in_play == True:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            else:
                d.draw(canvas,pos)
        elif 0<i<5:
            d.draw(canvas,pos)
                                               
            

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()