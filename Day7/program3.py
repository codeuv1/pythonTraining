# Find the maximum sum of any contiguous subarray of size 3

def maximum_sum(nums,k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k,len(nums)):
        curr_sum += nums[i] - nums[i-k]
        max_sum = max(curr_sum, max_sum)
    return max_sum

# Find the shortest subarray with a sum greater than or equal to $S$.
def solve(nums,k):
    min_len = float('inf')
    left = 0
    window_sum = 0
    l = r = -1
    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= k:
            curr_len = right - left + 1
            if min_len > curr_len:
                min_len = curr_len
                l = left
                r = right
            window_sum -= nums[left]
            left += 1

    return nums[l:r+1],min_len if min_len != float('inf') else None

# find all possible anagrams
def solve1(string , anagram):
    k , n  = len(anagram) , len(string)
    result = []
    if n < k:
        return result
    def index(char):
        return ord(char) - ord('a')

    anagram_map = [0] * 26
    curr_map = [0] * 26
    for i in range(k):
        anagram_map[index(anagram[i])] += 1
        curr_map[index(string[i])] += 1

    if curr_map == anagram_map:
        result.append(0)
    left = 0
    for right in range(k,n):
        curr_map[index(string[left])] -= 1
        left += 1
        curr_map[index(string[right])] += 1
        if curr_map == anagram_map:
            result.append(left)

    return [string[i : i + k] for i in result]

 # Given a string (e.g., "eceba") and an integer $k=2$
# , find the length of the longest substring that contains at most $k$ distinct characters.
def solve2(string):
    n = len(string)

    left = 0
    seen = set()
    l , r = 0 , 0
    max_len = float('-inf')
    for right in range(n):
        while string[right] in seen :
            seen.remove(string[left])
            left +=1
        seen.add(string[right])
        curr_len = right - left + 1
        if curr_len > max_len:
            max_len = curr_len
            l = left
            r = right
    return string[l : r + 1]

#jump optimization - when u see a duplicate jump left to last occurance
def solve3(string):
    left = 0
    seen = {}
    best_range = (0,0)
    max_len = float('-inf')
    for right,char in enumerate(string):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right

        curr_len = right - left + 1
        if curr_len > max_len:
            max_len = curr_len
            best_range = (left, right)
    l , r = best_range
    return string[l : r + 1]

#atmost k distinct elements
def solve4(string,k):
    left = 0
    seen = {}
    best_range = (0,0)
    max_len = float('-inf')
    for right,char in enumerate(string):
        seen[char] = seen.get(char,0) + 1
        while seen[char] > k:
            seen[char] -=1
            left += 1
        if char not in seen :
            seen[char] = 0

        curr_len = right - left + 1
        if curr_len > max_len:
            max_len = curr_len
            best_range = (left, right)
    left , right = best_range
    return string[left : right + 1]

def solve5(nums,k):
    left = 0
    best_range = (0,0)
    max_len = float('-inf')

    zero_count = 0
    for right,char in enumerate(nums):

        if nums[right] == 0:
            zero_count += 1

        while zero_count > k :
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        curr_len = right - left + 1
        if curr_len > max_len:
            max_len = curr_len
            best_range = (left, right)
    return nums[left : right + 1]

print(solve5([1,0,1,1,0,0,1],2))