import os
import re
import sys
import timeit
from typing import Set 

from levenshtein import levenshtein

from utils import clear

clear()  # clear the terminal screen.
input_word = input("\n\nPlease enter a word.\n")

if os.path.exists('/usr/dict/words'):
    path_to_words = '/usr/dict/words' 
elif os.path.exists('/usr/share/dict/words'):
    path_to_words = '/usr/share/dict/words'
else:
    sys.exit("Words file not found. Exiting...")

print(f"\nChecking {input_word} against words in {path_to_words}")

# Open and grab the words in the file as a set.
with open(path_to_words) as f:
    all_words_set = {line.strip().lower() for line in f}

def real_word(word):
    """Check if word is in word set. I.e. it's not a mispelled word. """
    if word in all_words_set:
        sys.exit(f"{word} is a real word!")

def closest_match(input_word: str, words: Set) -> str:
    real_word(input_word) 

    print("Calculating edit distance...")   

    # Compute the edit distance between the input word and all words.
    ld_values_list = [levenshtein(input_word, w) for w in words]
    
    # Merge the computed edit values list with the words list.
    ld_dict = dict(zip(ld_values_list, words))
   
    # Get the min value of the edit values list.
    min_key = min(ld_dict.keys())

    return ld_dict.get(min_key)

if __name__ == "__main__":
    start = timeit.default_timer() 
    closest_match = closest_match(input_word, all_words_set)
    print(f"\nDid you mean {closest_match}?")
    end = timeit.default_timer()
    print(f"---------------")
    
    print(f"https://www.merriam-webster.com/dictionary/{closest_match}\n")

    print(f'The function was called {levenshtein.calls} times.')
    print(f'Time taken: {end-start:.2f} seconds\n')

