'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return their indices as [index1, index2] (1-indexed). You may not use the same element twice. Use only constant extra space.

Example 1

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: numbers[1] + numbers[2] = 2 + 7 = 9.
'''

def two_sum(nums, target):
    l,r = 0, len(nums)-1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l+1, r+1]

        elif s < target:
            l+=1
        else:
            r-=1
        


nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))