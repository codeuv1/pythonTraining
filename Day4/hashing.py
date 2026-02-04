from itertools import accumulate
from collections import Counter

class Solution:

    def solve(self, A):
        # Calculate prefix sums (cumulative sum)
        ps = list(accumulate(A))
        print(ps)
        # Case 1: If any prefix sum is 0, subarray from start to i is 0
        if 0 in ps:
            return 1

        # Case 2: If a prefix sum repeats, subarray between those indices is 0
        c = Counter(ps)
        print(c)
        for k, v in c.items():
            if v >= 2:
                return 1

        return 0


s = Solution()
print(s.solve([1,2,3,4,5]))