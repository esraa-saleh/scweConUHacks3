from PyDictionary import PyDictionary
import json

dictionary=PyDictionary()

def get_meaning(word):
    if type(word) != str:
        print("err")
    else:
        return dictionary.meaning(word)['Noun'][0]
    
print(get_meaning("derivative"))