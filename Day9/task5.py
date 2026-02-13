# Write a snippet to demonstrate the use of list typing in
# data analytics for handling large data values.

def mean(nums: list[float | int]) -> float:
    return float(sum(nums)) / len(nums)

# print(mean([1,2,2.5,"abys"])) # error
print(mean([1,2,2.5])) # error
