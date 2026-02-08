def has_duplicate(events):
    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            if events[i] == events[j] :
                return True
    return False

#Optimized algorithm

def has_duplicate2(events):
    return len(events) != len(set(events))

events = [1, 2, 3, 4, 5, 6, 7, 8, 9,1]

print(has_duplicate(events))
print(has_duplicate2(events))