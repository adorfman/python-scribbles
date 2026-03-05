
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat' ]

def anagram_finder( words: list[str]  ):

    a_map = {k: None for k in range(len(words)//2)}

    for w in words:
        l = list(w)
        l.sort()
        h = ''.join(l)

        if h not in a_map:
            a_map[h] = []

        a_map[h].append(w)

    return [ a_map[k] for k in a_map if a_map[k] is not None ]


print(anagram_finder(words))
print(anagram_finder(['']))
