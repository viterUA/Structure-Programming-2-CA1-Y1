#CA 1 Structure progrtamming 2

#This program portion of 3 games of “Aces High”. Program begin by asking the user,
#to enter the names of the two players who will be playing the game on input dialogs.
#main function is data of the game
#The function dealCard() will generate a card randomly and return this card as a string
#displayCards function fill the inforamtion window, and after all games main function displays
#all results

#Name: Mykhailo Hnylytskyi

#Class: Computing 1 Year Group X

from tkinter import simpledialog, messagebox, Text, Tk

import random

def dealCard(rank, suit):

    ranks = (11 == "Jack", 12 == "Queen", 13 == "King", 14 == "Ace")
    rank = random.randint(2,14)

    if rank in ranks:

        rank = ranks(rank)
    suits = (1 == "Hearts", 2 == "Diamonds", 3 == "Clubs", 4 == "Spades")
    suit = suits(random.randint(1,4))

def displayCards(user1, user2, card1, card2, gameNumber,textArea):
    textArea.insert(f"game(gameNumber):\n")
    textArea.insert(f"(user1) (card1)\n")
    textArea.insert(f"(user2) (card2)\n")

    card1 = dealCard(rank, suit)
    card2 = dealCard(rank, suit)

    gameNumber += 1

    window = Tk()
    window.title("Aces High")
  

    textArea = Text(window,width=50,height=5,font=("courier", 12))

    textArea.pack()    

    textArea.insert("1.0", displayCards)
    
#main area of program

textAreaData = "%-10s%-15s%-15s\n\n" % \
               ("Game #","Player name","Card Dealt")

i = 1

while (i <= 3):

    user1 = simpledialog.askstring("Input", "Please enter the name of player 1")
    
    user2 = simpledialog.askstring("Input", "Please enter the name of player 2")

    messagebox.showinfo("Aces High", "Please hit return to continue ....")

    i += 1
    
window = Tk()
window.title("Aces High")
  

textArea = Text(window,width=50,height=5,font=("courier", 12))

textArea.pack()    

textArea.insert("1.0", textAreaData)
    
dealCard(rank, suit)
displayCards(user1, user2, card1, card2, gameNumber,textArea)

