import os
import logging
import timeit

from flask import flash

from app import app, cache
from app.levenshtein import levenshtein

# Current directory path.
dirname = os.path.dirname(__file__)

logger = logging.getLogger(__name__)

if os.path.exists('/usr/dict/words'):
    path_to_words = '/usr/dict/words' 
elif os.path.exists('/usr/share/dict/words'):
    path_to_words = '/usr/share/dict/words'
else:
    path_to_words = os.path.join(dirname, 'static/assets/words.txt') 

# Open and grab the words in the file as a set.
with open(path_to_words) as f:
    all_words_set = {line.strip().lower() for line in f}

def real_word(word):
    """Check if word is in word set. I.e. it's not a mispelled word. """
    return word in all_words_set

@cache.memoize(50)
def closest_match(input_word: str) -> str:
    start = timeit.default_timer()
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
    
    end = timeit.default_timer()
    
    if app.debug:
        flash(f'The function was called {levenshtein.calls} times', 'warning')
        flash(f'Time taken to execute function: {end-start:.2f} seconds', 'warning')

    return f'Did you mean {ld_dict.get(min_key)}?'

