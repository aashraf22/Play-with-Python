"""
A program which you can give a word, an English word and the program will 
return the definition of that word in English.
"""
#import data
import json
#to get the best matches of a word
from difflib import get_close_matches

#read the data into the program
data = json.load(open("data.json"))

def get_the_definition(word):
    #convert it to lowercase
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        match = input("Did you mean %s instead?Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if match == 'Y' or match == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif match == 'N' or match == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

choice = input("Enter a word or exit?Enter W to enter a word or anything else to exit")
while choice == 'W' or choice == 'w':
    word = input("Enter word: ")
    output = get_the_definition(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    choice = input("Enter a word or exit?Enter W to enter a word or anything else to exit")
        
