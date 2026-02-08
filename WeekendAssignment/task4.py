def longest_consecutive(nums):
    longest = 0
    for num in nums:
        length = 1
        while num + length in nums:
            length += 1
        longest = max(longest, length)
    return longest

def longest_consecutive2(nums):
    nums.sort()
    longest = 1
    curr = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            curr += 1
        else:
            longest = max(longest, curr)
            curr = 1
    return max(longest, curr)

nums = [7, 4, 6, 1, 3, 2, 8 ,9 ,10]
print(longest_consecutive(nums))
print(longest_consecutive2(nums))