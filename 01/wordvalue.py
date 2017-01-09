from data import DICTIONARY, LETTER_SCORES

LETTER_SCORES['-'] = 0

def load_words():
    with open(DICTIONARY) as f:
        content = f.read()
    return content.split('\n')

def calc_word_value(word):
    return sum(LETTER_SCORES.get(C) for C in word.upper())

def _max_word_value(words=load_words()):
    # Also works, but a tiny slowest
    # Sorting is n log n, but bound to O(n) from input list
    scores = [(-1 * calc_word_value(word),word) for word in words]
    scores.sort(key=lambda t: t[0])
    return scores[0][1]

def _max_word_value(words=load_words()):
    # Also works, but a tiny bit slower.
    # Sorting is n log n, but bound to O(n) from input list
    import heapq
    scores = [(-1 * calc_word_value(word),word) for word in words]
    heapq.heapify(scores)
    return scores[0][1]

def max_word_value(words=load_words()):
    # Best. Algorithm is bound to O(n)
    scores = ((calc_word_value(word),word) for word in words)
    return max(scores, key=lambda t: t[0])[1]


if __name__ == "__main__":
    pass