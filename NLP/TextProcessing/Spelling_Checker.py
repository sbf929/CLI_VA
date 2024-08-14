"""Contains function for checking the real meaning behind """
import difflib
from textblob import TextBlob

def get_closest_match(input_word:str, target_word:str):
    """ Checks if there is any word in `target_word` list that matches `input_word` and assigns its value to it. 
    `target_word needs to be a full string.`"""

    target_list = list(target_word)

    closest_matches = difflib.get_close_matches(input_word, target_list, n = 3, cutoff = 0.7)

    print(closest_matches)
    if closest_matches:
        return closest_matches[0]
    else:
        None

print(get_closest_match("prgram", "I can create a program in Python."))



def Autocorrect(input_word: str | list):
    """ Basic autocorrection for words. """
    
    blob = TextBlob(input_word)
    corrected_word = blob.correct()

    return str(corrected_word)
