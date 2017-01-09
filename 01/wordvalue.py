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
    scores = [(calc_word_value(word),word) for word in words]
    scores.sort(key=lambda t: t[0], reverse=True)
    return scores[0][1]

def _max_word_value(words=load_words()):
    # Also works, but a tiny bit slower.
    # Sorting is n log n, but bound to O(n) from input list
    # If already in heap, accessing the largest element is actually O(n)
    # Note that heapq is a priority queue, that sorts a binary heap
    # with the smallest element on top. I looked up on stackoverflow how to
    # make a maxheap: Simply invert the key -_-
    # http://stackoverflow.com/a/2501527/1203756
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