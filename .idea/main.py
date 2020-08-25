from random import randint

deck = []
hand = []

def create_deck():
  s = ""
  for suit in range(4):
    for num in range(1, 14):
      if suit == 0:
        s = "Hearts"
      elif suit== 1:
        s = "Diamonds"
      elif suit == 2:
        s = "Clubs"
      else:
        s = "Spades"
      if num == 11:
        num = "Jack"
      elif num == 12:
        num = "Queen"
      elif num == 13:
        num = "King"
      elif num == 1:
        num = "Ace"
      deck.append(str(num) + " of " + s)

def draw():
  x = randint(0, len(deck)-1)
  card = deck[x]
  deck.remove(card)
  return card

def roll_dice():
  sides = int(input("What size dice we rolling? "))
  num = int(input("How many dice we rolling? "))
  add = int(input("What are we adding to dice? (if nothing enter 0) "))
  dice = []
  for x in range(num):
    i = randint(1, sides)
    dice.append(i+add)
  print(dice)

def pick_card():
  num = int(input("How many cards would you like to draw? "))
  for x in range(num):
    hand.append(draw())
  print(hand)

create_deck()



while(True):
  print("What would you like to do?")
  print("A - roll dice")
  print("B - pick a card")
  choice = input()

  if choice == "A":
    roll_dice()
  elif choice == "B":
    pick_card()
  else:
    print("not a choice try again ")
    choice = input()