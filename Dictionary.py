from PyDictionary import PyDictionary
import json

dictionary=PyDictionary()

def get_meaning(word):
    if type(word) != str or len(word)==0:
        print("err")

    else:
        return list(dictionary.meaning(word).values())[0][0]
