'''
Given an integer array nums of length n, create an array ans of length 2n where ans[i] == nums[i] and ans[i+n] == nums[i] for all 0 ≤ i < n. Return ans.

Example 1

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: ans = nums + nums.
'''

def concatenation_of_array(nums):
    n = len(nums)
    res = [0] * (n*2)
    for i in range(n):
        res[i] = res[i+n] = nums[i]

    return res

nums = [1,2,1]
print(concatenation_of_array(nums))
