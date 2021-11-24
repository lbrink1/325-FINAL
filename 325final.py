#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## TRANSLATOR CODE: LOREN
  
#random word generator library 
import random
     
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

    #Turns all lowercases that were input to uppercase so translation can be used
    english = english.upper() 
    
    #Preallocate string for translation
    morsefromenglish= ""
    
    #For every letter in string, convert to morse and add to morsefromenglish string
    for i in english:
        morsefromenglish += translation[i] + " "
    return morsefromenglish

# Prompts user to input english to translate
english = input("Enter English to translate to morse code: ")
    
#Call translator to translate english to morse code
morsefromenglish = translate_english(english)   

#Print translation to the user 
print(morsefromenglish)

#####################################################


## GAME CODE : LOREN / SEBASTIAN
difficulty = input("What level of difficulty would you like to play? Please enter easy or hard: ")


while difficulty == 'easy':
    
    learningeasy= {"-.-- . ...":"yes",
                   "-.. --- --.":"dog" ,
                   "-.-. .- -":"cat",
                   "... . .-":"sea",
                   "..-. --- -..-":"fox",
                   "- .-. . .":"tree",
                    ".-. .- - .":"rate",
                    "- .... .":"the",
                    ".- -. -..":"and",
                    "-. ---":"no",
                    "-.- . -.--":"key",
                    ".-- .... -.--":"why",
                    "... ..- -.": "sun"
                    }

    easy = list(learningeasy.keys())
    random.shuffle(easy) 
    
    correctanswers = 0
    wronganswers = 0
    
    for keyword in easy:
        rightwrong = "{}"
        print(rightwrong.format(keyword))
        answer= input("What is this in English? Enter in all lowercase: ")
        print(" ")
        
        if answer == (learningeasy[keyword]):
            print("Correct answer!")
            correctanswers += 1
        else: 
            print("Wrong answer.")
            wronganswers += 1
            
    rightwrong = "Your score is {}/{}"

    print(rightwrong.format(correctanswers,wronganswers))  
      
    break
   
else:
    
    learninghard = {"... -.-. .... --- --- .-..": "school", 
                    ".--. .-. --- .--- . -.-. -":"project",
                    "..-. .. ... ....":"fish", 
                    "-- --- - .... . .-.": "mother", 
                    "..-. .- - .... . .-.":"father",
                    "..-. .. -. .- .-..":"final", 
                    "... -.-. --- .-. .":"score",
                    "- .. .-. . -..":"tired",
                    "... .-.. . . .--.":"sleep",
                    "--. .-. . . -.":"green",
                    "... -.- .- - .":"skate",
                    "-... .-. . .- -.-":"break",
                    "... ..- -. -.. .- -.--":"sunday",
                
                 }

hard = list(learninghard.keys())

random.shuffle(hard) 
    
correct_answers = 0
wrong_answers = 0
    
for keyword in hard:
    right_wrong = "{}"
    print(right_wrong.format(keyword))
    answer= input("What is this in English? Enter in all lowercase: ")
        
    if answer == (learninghard[keyword]):
        print("Correct answer!")
        correct_answers += 1
    else: 
        print("Wrong answer.")
        wrong_answers += 1
            
    right_wrong = "Your score is {}/{}"
    
print(right_wrong.format(correct_answers,wrong_answers))  
difficulty = input("Want to try again? To continue, enter 'easy' or 'hard'. If you recieve a perfect score of 13/13 on 'easy' mode, type 'hard' to move on to a more difficult level: ")

    
        
## GUI CODE: SEBASTIAN
