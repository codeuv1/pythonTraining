from _collections import deque


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
    left = 0
    queue = deque([index for index,num in enumerate(nums[:k]) if num < 0])
    for right in range(k,len(nums)):
        if nums[right] < 0:
            queue.append(right)
        if queue and queue[0] == left:
            queue.popleft()
        if len(queue) > 0:
            print(nums[queue[0]],end=" ")
        else:
            print(0,end=" ")

        left+=1


print(firstNegative([12,-1,-7,8,-15,30,16,28],3))