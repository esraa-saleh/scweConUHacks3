from PyDictionary import PyDictionary
import json

dictionary=PyDictionary()

def get_meaning(word):
    if type(word) != str or len(word)==0:
        return "meaning not found"
    else:
        return list(dictionary.meaning(word).values())[0][0]
