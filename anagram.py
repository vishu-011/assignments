def anagram(l):
    groups = {}
    for word in l:
        key = "".join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    print(groups)
    return list(groups.values())
    

f = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(anagram(f))
