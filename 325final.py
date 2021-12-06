#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

## TRANSLATOR CODE: LOREN
  
#random word generator library 
import random
root = Tk()
     
#Using dictionaries for translation A-Z, 0-9
translation = {"A": ".-",
               "B": "-...",
               "C": "-.-.",
               "D": "-..",
               "E": ".",
               "F": "..-.",
               "G": "--.",
               "H": "....",
               "I": "..",
               "J": ".---",
               "K": "-.-",
               "L": ".-..",
               "M": "--",
               "N": "-.",
               "O": "---",
               "P": ".--.",
               "Q": "--.-",
               "R": ".-.",
               "S": "...",
               "T": "-",
               "U": "..-",
               "V": "...-",
               "W": ".--",
               "X": "-..-",
               "Y": "-.--",
               "Z": "--..",
               "1": ".----",
               "2": "..---",
               "3": "...--",
               "4": "....-",
               "5": ".....",
               "6": "-....",
               "7": "--...",
               "8": "---..",
               "9": "----.",
               "0": "-----",
               " ": " " # space for sentence translations
              
                }

def translate_english(english):
    '''
    Translates from English to morse code by using the dictionary
    from translation above. Takes in string as an input and will translate
    string to morse given that string input is not empty and does not contain
    any symbols. Can include spaces for sentences.

    '''

    # Turns all lowercases that were input to uppercase so translation can be used
    english = english.upper()

    # Preallocate string for translation
    morsefromenglish = ""

    # For every letter in string, convert to morse and add to morsefromenglish string
    for i in english:
        morsefromenglish += translation[i] + " "
    e2["text"] = morsefromenglish
    return morsefromenglish

#####################################################

def copy():
    # copying
    root.clipboard_clear()
    root.clipboard_append(e2["text"])


## GAME CODE : LOREN / SEBASTIAN

buttonpressed = StringVar()

#input("Want to try again? To continue, enter 'easy' or 'hard'. If you recieve a perfect score of 13/13 on 'easy' mode, type 'hard' to move on to a more difficult level. If you want to stop playing, type 'stop'.")
#difficulty = input("What level of difficulty would you like to play? Please enter easy or hard: ")
def play(difficulty):
    while difficulty == 'easy':
        learningeasy = {"-.-- . ...": "yes",
                        "-.. --- --.": "dog",
                        "-.-. .- -": "cat",
                        "... . .-": "sea",
                        "..-. --- -..-": "fox",
                        "- .-. . .": "tree",
                        ".-. .- - .": "rate",
                        "- .... .": "the",
                        ".- -. -..": "and",
                        "-. ---": "no",
                        "-.- . -.--": "key",
                        ".-- .... -.--": "why",
                        "... ..- -.": "sun"
                        }
        easy = list(learningeasy.keys())
        random.shuffle(easy)

        correctanswers = 0
        wronganswers = 0
        total = 13

        for keyword in easy:
            b7.place(x=625, y=175)
            labelAndAnswer()
            e5["text"] = keyword
            b7.wait_variable(buttonpressed)
            answer = e4.get()
            if answer == (learningeasy[keyword]):
                correctanswers += 1
                scoreLabel.config(text=str(correctanswers) + "/13")
                e4.delete(0, END)
            else:
                if correctanswers == 0:
                    scoreLabel.config(text=str(correctanswers) + "/13")
                else:
                    correctanswers -= 1
                    scoreLabel.config(text=str(correctanswers) + "/13")
                e4.delete(0, END)
        break

    else:

        learninghard = {"... -.-. .... --- --- .-..": "school",
                        ".--. .-. --- .--- . -.-. -": "project",
                        "..-. .. ... ....": "fish",
                        "-- --- - .... . .-.": "mother",
                        "..-. .- - .... . .-.": "father",
                        "..-. .. -. .- .-..": "final",
                        "... -.-. --- .-. .": "score",
                        "- .. .-. . -..": "tired",
                        "... .-.. . . .--.": "sleep",
                        "--. .-. . . -.": "green",
                        "... -.- .- - .": "skate",
                        "-... .-. . .- -.-": "break",
                        "... ..- -. -.. .- -.--": "sunday",

                        }

        hard = list(learninghard.keys())

        random.shuffle(hard)

        correct_answers = 0
        wrong_answers = 0
        total_answers = 13

        for keyword in hard:
            b7.place(x=625, y=175)
            labelAndAnswer()
            e5["text"] = keyword
            b7.wait_variable(buttonpressed)
            answer = e4.get()
            if answer == (learninghard[keyword]):
                correct_answers += 1
                scoreLabel.config(text=str(correct_answers) + "/13")
                e4.delete(0, END)
            else:
                if correct_answers == 0:
                    scoreLabel.config(text=str(correct_answers) + "/13")
                else:
                    correct_answers -= 1
                    scoreLabel.config(text=str(correct_answers) + "/13")
                e4.delete(0, END) 
        
## GUI CODE: SEBASTIAN

def difficulties():
    easyButton = Button(root, text="Easy Difficulty", width=10)
    easyButton.place(x=575, y=90)
    hardButton = Button(root, text="Hard Difficulty", width=10)
    hardButton.place(x=675, y=90)
    easyButton.config(
        command=lambda: [easyButton.destroy(), hardButton.destroy(), b4.destroy(), play('easy'), labelAndAnswer()])
    hardButton.config(
        command=lambda: [easyButton.destroy(), hardButton.destroy(), b4.destroy(), play('hard'), labelAndAnswer()])


def checkIfCorrect(answer, input1):
    if answer == input1:
        print("Correct!")


def labelAndAnswer():
    e3 = Label(root, text="What is this in English?", width=20, font=('Helvetica 25 bold'))
    e3.place(x=550, y=70)
    canvas.create_window(690, 150, window=e4)
    e6 = Label(canvas, text="Your score for the game is " + str(scoreLabel.cget("text")), width=50,
               font=('Helvetica 15'))
    e6.place(x=465, y=200)


def tutorial():
    textInput = str(e1.get())

root.geometry("900x400")

root.title("Morse Code Learner & Visualizer")

canvas = Canvas(root, width=1000, height=750, bg="white")
canvas.create_text(230, 70, text="Morse Code Learner", fill="black", font=('Helvetica 40 bold'))
canvas.create_text(230, 110, text="and Visualizer", fill="black", font=('Helvetica 40 bold'))

canvas.create_text(230, 175, text="Insert Text Here", fill="black", font=('Helvetica 15'))
e1 = Entry(canvas, width=25)
canvas.create_window(230, 200, window=e1)
b1 = Button(root, text='Convert', command=lambda: translate_english(e1.get()), width=10)
b1.place(x=180, y=230)

canvas.create_text(230, 280, text="Converted Morse Code", fill="black", font=('Helvetica 15'))
e2 = Label(root, text="", width=20)
e2.place(x=140, y=300)

b2 = Button(root, text='Copy to Clipboard', command=copy, width=15)
b2.place(x=70, y=340)

b3 = Button(root, text='Tutorial', command=copy, width=15)
b3.place(x=250, y=340)

b4 = Button(root, text='Play Learning Game!', command=difficulties, width=15)
b4.place(x=600, y=50)

e5 = Label(canvas, text="", width=20, font=('Helvetica 20 bold'))
e5.place(x=575, y=102.5)

scoreLabel = Label(canvas, text="0/13", width=20, font=('Helvetica 15'))

e4 = Entry(canvas, width=25)

b4.place(x=600, y=50)

b7 = Button(root, text='Am I correct?', command=lambda: buttonpressed.set("button pressed"), width=15)

canvas.pack()

root.mainloop()
