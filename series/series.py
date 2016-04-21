

def slices(s, length):
    if length == 0 or length > len(s):
        raise ValueError("Invalid input")
    strings = []
    for n in range(0, len(s)):
        if len(s) - n >= length:
          strings.append(split(s[n:n+length],1))
    return strings

def split(str, num):
    return [ int(str[start:start+num]) for start in range(0, len(str), num) ]
