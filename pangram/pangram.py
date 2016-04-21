import string

def is_pangram(str):
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter not in str.lower():
            return False
    return True
