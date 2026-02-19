from collections import defaultdict
def group_anagrams(words):
    groups = []
    for w in words:
        placed = False
        for g in groups:
            if sorted(w) == sorted(g[0]):
                g.append(w)
                placed = True
                break
        if not placed:
            groups.append([w])

    return groups

def group_anagrams2(words):
    anagram_map = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

words = ['bun','nub','tea','eat','ate','bed','edb']

print(group_anagrams(words))
print(group_anagrams2(words))