#Import List
from tkinter import *
from random import randint
from tkinter import font
from turtle import color
from tkinter import ttk
import random
from PIL import ImageTk,Image



#Basics
root = Tk()
root.title("Rock Paper Scissors -Made by Trapgrave")
root.iconbitmap("c:/images/star.ico")
root.config(bg="white")

    #Images
rock = PhotoImage(file="c:/images/rock.png")
paper = PhotoImage(file="c:/images/paper.png")
scissors = PhotoImage(file="c:/images/scissors.png")
    #-
Choose = Label(root, font=("Roboto", 15), text = "Rock, Paper, Scissors!", bg="white").pack(side = TOP)


    #Storing points

user_points = 0
computer_points = 0

    #Options
def Game(player_choice_string):
    print("player chose: {}".format(player_choice_string))



    
        





(RockButton := Button(root, image = rock, bg="white", bd=0,command=lambda:Game("rock"))).pack(side = LEFT)
(PaperButton := Button(root, image = paper, bg="white", bd=0,command=lambda:Game("paper"))).pack(side = RIGHT)
(ScissorsButton := Button(root, image = scissors, bg="white", bd=0, command=lambda:Game("scissors"))).pack(pady=10)


win_lose_tie_label = Label(root, text="", font=("Verdana", 15), bg = "white", bd=0).pack()

root.geometry("500x500")
root.mainloop()
