from collections import deque


def subarraySum( nums, k):

    left = 0
    curr_sum = max_sum = sum(nums[:k])

    for right in range(k,len(nums)):
        curr_sum += nums[right] - nums[left]
        max_sum = max(curr_sum,max_sum)
        left += 1
    return max_sum

def countAnagrams( string, anagram):
    def index(char):
        return ord(char) - ord('a')
    k = len(anagram)
    n = len(string)
    count = 0
    anagram_map = [0]*26
    string_map = [0]*26
    for i in range(k):
        anagram_map[index(anagram[i])] += 1
        string_map[index(string[i])] += 1
    left = 0
    for right in range(k,n):
        if anagram_map == string_map:
            count += 1
        string_map[index(string[left])] -= 1
        string_map[index(string[right])] += 1
        left += 1

    if anagram_map == string_map:
        count += 1

    return count


def firstNegative(nums, k):
    q = deque()

    for i in range(len(nums)):
        if nums[i] < 0:
            q.append(i)

        if q and q[0] <= i - k:
            q.popleft()

        if i >= k - 1:
            print(nums[q[0]] if q else 0, end=" ")


def maximum_subarray(nums,k):
    left = 0
    for right in range(k,len(nums)):
        print(max(nums[left:right]),end=" ")
        left += 1
    print(max(nums[left:]),end=" ")


maximum_subarray([12,-1,-7,8,-15,30,16,28],3)