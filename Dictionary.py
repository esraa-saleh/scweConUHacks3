from PyDictionary import PyDictionary
import json

dictionary=PyDictionary()

def get_meaning(word):
    print("Printing the word: ",word)
    if type(word) != str:
        print("err")
    else:
        return list(dictionary.meaning(word).values())[0][0]
