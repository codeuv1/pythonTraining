def reverse(row):
    start = 0
    end = len(row) - 1

    while start < end:
        row[start], row[end] = row[end], row[start]
        start += 1
        end -= 1

def rotate_180(matrix):
    matrix.reverse()

    for row in matrix:
        row.reverse()

    for row in matrix:
        print(row)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(rotate_180(matrix))