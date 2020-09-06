from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
content = ttk.Frame(root)
content.grid(column=0, row=0)

deck = []
hand = []


def create_deck():
    s = ""
    for suit in range(4):
        for num in range(1, 14):
            if suit == 0:
                s = "Hearts"
            elif suit == 1:
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


def clear(object):
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()


def roll(num, size, add):
    clear(content)
    dice = []
    for x in range(num):
        i = randint(1, size)
        dice.append(i)
    # print(dice)
    dice_label = ttk.Label(content, text=dice)
    dice_label.grid(column=0, row=0)
    total = 0
    for x in dice:
        total += x
    total += add
    dice_total = ttk.Label(content, text=("Total: " + str(total)))
    dice_total.grid(column=0, row=1)
    average = total / num
    dice_avg = ttk.Label(content, text=("Average: " + str(average)))
    dice_avg.grid(column=1, row=1)
    home_btn = ttk.Button(content, text="Roll Again", command=dice_roller)
    home_btn.grid(column=0, row=2)


def dice_roller():
    clear(content)
    label = ttk.Label(content, text="Dice Roller")
    label.grid(column=0, row=0, columnspan=6)
    myCanvas = Canvas(content, bg="white", height=200, width=1200)
    d4 = myCanvas.create_polygon(10, 190,
                                 100, 10,
                                 190, 190,
                                 fill="white",
                                 outline="black")
    d4Text = myCanvas.create_text(100, 100, text="d4")
    d6 = myCanvas.create_rectangle(200, 190,
                                   390, 10,
                                   fill="white",
                                   outline="black")
    d6Text = myCanvas.create_text(280, 100, text="d6")
    d8 = myCanvas.create_polygon(400, 150,
                                 400, 50,
                                 490, 10,
                                 580, 50,
                                 580, 150,
                                 490, 190,
                                 fill="white",
                                 outline="black")
    d8Text = myCanvas.create_text(490, 100, text="d8")
    d10 = myCanvas.create_polygon(600, 130,
                                  600, 70,
                                  695, 10,
                                  790, 70,
                                  790, 130,
                                  695, 190,
                                  fill="white",
                                  outline="black")
    d10Text = myCanvas.create_text(695, 100, text="d10")
    d12 = myCanvas.create_polygon(923, 14,
                                  867, 14,
                                  822, 47,
                                  805, 100,
                                  822, 153,
                                  867, 186,
                                  923, 186,
                                  968, 153,
                                  985, 100,
                                  968, 47,
                                  923, 14,
                                  fill="white",
                                  outline="black")
    d12Text = myCanvas.create_text(895, 100, text="d12")
    d20 = myCanvas.create_polygon(1140, 22,
                                  1050, 22,
                                  1005, 100,
                                  1050, 178,
                                  1140, 178,
                                  1185, 100,
                                  1140, 22,
                                  fill="white",
                                  outline="black")
    d4Text = myCanvas.create_text(1095, 100, text="d20")
    myCanvas.grid(column=0, row=1, columnspan=6)
    d4_btn = ttk.Button(content, text="d4", command=(lambda: (size_dice_entry.delete(0, END),
                                                              size_dice_entry.insert(0, "4"))))
    d4_btn.grid(column=0, row=2)
    d6_btn = ttk.Button(content, text="d6", command=(lambda: (size_dice_entry.delete(0, END),
                                                              size_dice_entry.insert(0, "6"))))
    d6_btn.grid(column=1, row=2)
    d8_btn = ttk.Button(content, text="d8", command=(lambda: (size_dice_entry.delete(0, END),
                                                              size_dice_entry.insert(0, "8"))))
    d8_btn.grid(column=2, row=2)
    d10_btn = ttk.Button(content, text="d10", command=(lambda: (size_dice_entry.delete(0, END),
                                                                size_dice_entry.insert(0, "10"))))
    d10_btn.grid(column=3, row=2)
    d12_btn = ttk.Button(content, text="d12", command=(lambda: (size_dice_entry.delete(0, END),
                                                                size_dice_entry.insert(0, "12"))))
    d12_btn.grid(column=4, row=2)
    d20_btn = ttk.Button(content, text="d20", command=(lambda: (size_dice_entry.delete(0, END),
                                                                size_dice_entry.insert(0, "20"))))
    d20_btn.grid(column=5, row=2)

    num_dice = IntVar()
    num_dice.set(1)
    num_dice_entry = ttk.Entry(content, textvariable=num_dice)
    num_dice_entry.grid(column=0, row=3)
    # num_dice_entry.insert(0, "1")

    dice_label = ttk.Label(content, text=" d ")
    dice_label.grid(column=1, row=3)

    size_dice = IntVar()
    size_dice.set(6)
    size_dice_entry = ttk.Entry(content, textvariable=size_dice)
    size_dice_entry.grid(column=2, row=3)
    # size_dice_entry.insert(0, "6")

    add_label = ttk.Label(content, text=" + ")
    add_label.grid(column=3, row=3)

    add_box = IntVar()
    add_box.set(0)
    add_box_entry = ttk.Entry(content, textvariable=add_box)
    add_box_entry.grid(column=4, row=3)
    # add_box_entry.insert(0, "0")

    roll_btn = ttk.Button(content, text="Roll", command=lambda: roll(num_dice.get(), size_dice.get(), add_box.get()))
    roll_btn.grid(column=5, row=3)

    # dice roller


def draw():
    try:
        x = randint(0, len(deck) - 1)
        card = deck[x]
        deck.remove(card)
        return card
    except:
        return "Deck Empty"


def pick_card(num):
    clear(content)
    empty_label = ttk.Label(content, text="Deck Empty")
    for x in range(num):
        card = draw()
        if card != "Deck Empty":
            hand.append(draw())
        else:
            empty_label.grid(column=0, row=1, columnspan=2)
            #print("Deck Empty")
            break
    hand_label = ttk.Label(content, text="Drawn: ")
    hand_label.grid(column=0, row=0)
    card_print = ttk.Label(content, text=hand)
    card_print.grid(column=1, row=0)
    home_btn = ttk.Button(content, text="Draw Again", command=card_picker)
    home_btn.grid(column=0, row=2, columnspan=2)


def card_picker():
    clear(content)
    label = ttk.Label(content, text="Card Picker")
    label.grid(column=0, row=0, columnspan=2)
    card_ask = ttk.Label(content, text="How many cards would you like draw?")
    card_ask.grid(column=0, row=1, columnspan=2)
    num_card = IntVar()
    num_card.set(1)
    num_card_entry = ttk.Entry(content, textvariable=num_card)
    num_card_entry.grid(column=0, row=2)
    draw_btn = ttk.Button(content, text="Draw", command=lambda: pick_card(num_card.get()))
    draw_btn.grid(column=1, row=2)
    # card picker


def main_screen():
    clear(content)
    create_deck()
    dice_photo = PhotoImage(file='dice_resized.png')
    dice = Button(content, image=dice_photo, width=200, height=200, command=dice_roller)
    dice.image = dice_photo
    dice.grid(column=0, row=0)
    label = ttk.Label(content, text="OR")
    label.grid(column=1, row=0)
    card_photo = PhotoImage(file='card_resized.png')
    card = Button(content, image=card_photo, width=200, height=200, command=card_picker)
    card.image = card_photo
    card.grid(column=2, row=0)


main_screen()
root.mainloop()
