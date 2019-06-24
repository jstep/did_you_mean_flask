def call_counter(func):
    # Decorator used for debugging how many times a function was called.
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__
    return helper

def memoize(func):
    """Saves already compute values to speed up levenshtein function."""
    mem = {}
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]
    return memoizer

@call_counter
@memoize    
def levenshtein(seq1: str, seq2: str) -> int:
    """Recursively compute the edit distance of two strings."""
    if seq1 == "":
        return len(seq2)
    if seq2 == "":
        return len(seq1)
    if seq1[-1] == seq2[-1]:
        cost = 0
    else:
        cost = 1
    
    result = min([levenshtein(seq1[:-1], seq2) + 1,
               levenshtein(seq1, seq2[:-1]) + 1,
               levenshtein(seq1[:-1], seq2[:-1]) + cost ])
    return result

