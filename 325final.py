#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## TRANSLATOR CODE: LOREN
        
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
english = input("Enter English to translate to morse code:")
    
#Call translator to translate english to morse code
morsefromenglish = translate_english(english)   

#Print translation to the user 
print(morsefromenglish)

#####################################################


## GAME CODE : SEBASTIAN/LORhEN



## GUI CODE: SEBASTIAN
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


## TRANSLATOR CODE: LOREN

#
class morse_code:
    def __init__(self):
        
        '''
        Class morse_code docstring 
        
        '''
        
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
              
                }

def translator(self,translation):
   
    '''
    Add docstring 
    '''
    


## GAME CODE : SEBASTIAN/LOREN



## GUI CODE: SEBASTIAN


