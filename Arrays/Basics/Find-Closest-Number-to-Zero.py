'''Given an integer array nums, return the number with the smallest absolute value. If there is a tie, return the positive number.

Example 1

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation: |1|=1 is smallest.


Example 2

Input: nums = [2,-1,1]
Output: 1
Explanation: |-1|=|1|=1 (tie) → return positive: 1.
'''

def find_closest_number(nums):
    res = nums[0]
    for num in nums[1:]:
        if abs(res) > abs(num):
            res = num

        elif abs(res) == abs(num) and num > 0:
            res = num
    
    return res

nums = [-4,-2,1,4,8]
print(find_closest_number(nums))