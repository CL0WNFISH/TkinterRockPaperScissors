#Import List
from ast import Delete
from sqlite3 import Row
from tkinter import *
from random import randint
from tkinter import font
from tkinter.tix import COLUMN
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
rock = PhotoImage(file="c:/images/rock.png")
paper = PhotoImage(file="c:/images/paper.png")
scissors = PhotoImage(file="c:/images/scissors.png")
    #-
Choose = Label(root, font=("Roboto", 15), text = "Rock, Paper, Scissors!", bg="white").pack(side = TOP)

    #Storing points
user_points = 0
computer_points = 0
    #Options

def Delete():
    user_points.destroy()
    win_lose_tie_label.destroy()
def Game(player_choice_string):
    print("player chose: {}".format(player_choice_string))







    global user_points, computer_points

    options = ["rock", "paper", "scissors"]
    computer_input = random.choice(options)

    if player_choice_string == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie!")
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("you lost!")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("you win!")
            user_points += 1

    elif player_choice_string == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You win!")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It is a tie!")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("you lost!")
            user_points += 1

    elif player_choice_string == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("You lost!")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You win!")
            user_points += 1
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It is a tie!")   
    global points_label
    global win_lose_tie_label
    points_label = Label(root, text="You have "+ str(user_points) + " and the enemy now has: " + str(computer_points) + "!", bg="white", bd=0).pack()
    win_lose_tie_label = Label(root, text="Your choice was: "+player_choice_string+" and the enemy's choice was: "+computer_input, font=("Verdana", 5),bg = "white", bd=0).pack()


(RockButton := Button(root, image = rock, bg="white", bd=0,command=lambda:Game("rock"))).pack(side = LEFT)
(PaperButton := Button(root, image = paper, bg="white", bd=0,command=lambda:Game("paper"))).pack(side = RIGHT)
(ScissorsButton := Button(root, image = scissors, bg="white", bd=0, command=lambda:Game("scissors"))).pack(pady=10)

root.geometry("500x500")
root.mainloop()

























