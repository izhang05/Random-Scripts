map = {";": "q", ",": "w", ".": "e", "p": "r", "y": "t", "f": "y", "g": "u", "c": "i", "r": "o", "l": "p", "a": "a",
       "o": "s", "e": "d", "u": "f", "i": "g", "d": "h", "h": "j", "t": "k", "n": "l", "s": ";", "'": "z", "q": "x",
       "j": "c", "k": "v", "x": "b", "b": "n", "m": "m", "w": ",", "v": ".", "z": "/"}


def convert(s):
    res = ""
    for i in s:
        res += map[i]
    return res