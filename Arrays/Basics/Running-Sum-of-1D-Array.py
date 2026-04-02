'''
Given an array nums, define its running sum as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

Example 1

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum: 1, 1+2=3, 1+2+3=6, 1+2+3+4=10.
'''

def running_sum(nums):
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]

    return nums

nums = [1,2,3,4]
print(running_sum(nums))