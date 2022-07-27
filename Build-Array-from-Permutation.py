"""
 Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

print(11//3) #3
print(11%3)  #2

ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
ans  = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
[0, 1, 2, 4, 5, 3]
 """

import time


nums = [0,2,1,5,3,4]




def buildArray(nums):
    q = len(nums)
    print(q)
    for i,c in enumerate(nums):
        nums[i] += q * (nums[c] % q)
    print(nums)
    for i,_ in enumerate(nums):
        # floor division
        nums[i] //= q
    return nums




   
 
start = time.process_time()
print(buildArray(nums))

print(f"Task took {time.process_time() - start}")




