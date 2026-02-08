def has_overlap(intervals):
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i][1] > intervals[j][0]:
                return True
    return False

def has_overlap2(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1,len(intervals)):
        if intervals[i - 1][1] > intervals[i][0]:
            return True
    return False

intervals = [[5, 10], [1, 4], [19, 20]]

print(has_overlap2(intervals))
print(has_overlap2(intervals))