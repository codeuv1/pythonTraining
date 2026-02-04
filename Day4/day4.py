from collections import deque
nums = [1,3,-1,-3,3,5,3,6,7]
k = 3
dq = deque()
# dq will store the index

for i in range(len(nums)):
    print([nums[j] for j in dq])
    # dq[0] left
    # if dq is present and dq of left
    if dq and dq[0] <= i-k:
        dq.popleft()
    # dq[-1] end element
    while dq and nums[dq[-1]] < nums[i]:
        dq.pop()
    dq.append(i)
    if i >= k-1:
        print(nums[dq[0]], end=" ")


