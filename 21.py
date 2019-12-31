from tkinter import *
import random
from threading import Thread
from playsound import playsound

class Player:
    def __init__(self, name, cash):
        self.__name = name
        self.__cash = cash
    def add_money(self, money):
        self.__cash += money
    def get_money(self):
        return self.__cash

def part1():
    lbl1.grid_forget()
    txt1.grid_forget()
    btn1.grid_forget()
window = Tk()
window.title("Blackjack")
lbl1 = Label(window, text="What is your name?", font=("Sheriff", 40))
lbl1.grid(column=0, row=0)
txt1 = Entry(window,width=20)
txt1.focus()
txt1.grid(column=0, row=1)
btn1 = Button(window, text="Enter", fg="white", command=part1)
btn1.grid(column=0, row=2)
nameplayer = str(txt1.get())
player1 = Player(nameplayer, 15000)
player1.add_money(5000)
dealer = Player("Dealer", 9999999)

lbl2 = Label(window, text=str(player1.get_money()) + "$").grid(column=2, row=2, sticky=E)


window.geometry('800x400')

window.mainloop()
"""
def flip_sound():

def winner_sound():

def hit():

def fold():

def double():
"""