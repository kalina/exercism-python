

def detect_anagrams(test_word, words):
    anagrams = []

    words = [x for x in words if len(x) == len(test_word) and x.lower() != test_word.lower()]

    test_count = count_chars(test_word)
    for word in words:
        if count_chars(word) == test_count:
            anagrams.append(word)
    return anagrams


def count_chars(word):
    counts = dict()
    for letter in word.lower():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts
