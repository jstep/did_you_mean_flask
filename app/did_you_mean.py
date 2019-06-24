import os
import timeit
import logging

from app.levenshtein import levenshtein


logger = logging.getLogger(__name__)

if os.path.exists('/usr/dict/words'):
    path_to_words = '/usr/dict/words' 
elif os.path.exists('/usr/share/dict/words'):
    path_to_words = '/usr/share/dict/words'
else:
    path_to_words = './static/assests/words.txt'

# Open and grab the words in the file as a set.
with open(path_to_words) as f:
    all_words_set = {line.strip().lower() for line in f}

def real_word(word):
    """Check if word is in word set. I.e. it's not a mispelled word. """
    return word in all_words_set

def closest_match(input_word: str) -> str:
    logger.debug(f"\nChecking {input_word} against words in {path_to_words}")
    
    if real_word(input_word):
        return f'{input_word} is a real word!'

    logger.debug("Calculating edit distance...")   

    # TODO: this is slow and could use some optimization. Maybe break out
    # early if the edit distance is computed to be 1.
    # Compute the edit distance between the input word and all words.
    ld_values_list = [levenshtein(input_word, w) for w in all_words_set]
    
    # Merge the computed edit values list with the words list.
    ld_dict = dict(zip(ld_values_list, all_words_set))
   
    # Get the min value of the edit values list.
    min_key = min(ld_dict.keys())

    return f'Did you mean {ld_dict.get(min_key)}?'

#if __name__ == "__main__":
#    start = timeit.default_timer() 
#    closest_match = closest_match(input_word, all_words_set)
#    print(f"\nDid you mean {closest_match}?")
#    end = timeit.default_timer()
#    print(f"---------------")
    
#    print(f"https://www.merriam-webster.com/dictionary/{closest_match}\n")

#    print(f'The function was called {levenshtein.calls} times.')
#    print(f'Time taken: {end-start:.2f} seconds\n')

