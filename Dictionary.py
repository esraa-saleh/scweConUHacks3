from PyDictionary import PyDictionary
import json

dictionary=PyDictionary()

def get_meaning(word):
<<<<<<< HEAD
    if type(word) != str or len(word)==0:
=======
    print("Printing the word: ",word)
    if type(word) != str:
>>>>>>> 6ef61e36ccd2e4e26bf4f14e4ce45995623cff25
        print("err")

    else:
        return list(dictionary.meaning(word).values())[0][0]
