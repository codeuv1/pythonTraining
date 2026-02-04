def flip_zeroes(nums,k):
    start = 0
    max_ones = 0
    curr_zeroes = 0


    for end in range(len(nums)):
        if nums[end] == 0:
            curr_zeroes += 1
        # when this condition satisfies - it means we have encountered a new zero
        # so move start
        while curr_zeroes > k:
            if nums[start] == 0:
                curr_zeroes -= 1
            start += 1

        max_ones = max(max_ones, end-start+1)
    return max_ones

print(flip_zeroes([1,0,0,1,0,1],1))