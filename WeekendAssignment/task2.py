def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

def two_sum2(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        if target - num in seen:
            return seen[target - num], i
        seen[num] = i

print(two_sum([1, 2, 3, 7], 8))
print(two_sum2([1, 2, 3, 7], 8))
