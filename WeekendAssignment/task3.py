from collections import defaultdict

nums = [1, 2, 3, -2, 5]
k = 3
def subarray_sum(nums,k):
    count = 0

    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if s == k:
                count += 1
    return count

def subarray_sum2(nums, k):
    count = 0
    current_sum = 0
    sum_frequencies = defaultdict(int)
    sum_frequencies[0] = 1
    for num in nums:
        current_sum += num
        if (current_sum - k) in sum_frequencies:
            count += sum_frequencies[current_sum - k]
        sum_frequencies[current_sum] += 1
    return count

print(subarray_sum(nums, 3))
print(subarray_sum2(nums, 3))