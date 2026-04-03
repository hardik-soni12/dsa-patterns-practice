'''
Given a sorted integer array nums, remove duplicates in-place such that each unique element appears only once. Return the count of unique elements k. The first k elements of nums must hold the unique values.

Example 1
Input: nums = [1,1,2]
Output: k=2, nums=[1,2,_]
'''
def removeDuplicates(nums):
    k = 0
    for i in range(1,len(nums)):
        if nums[k] != nums[i]:
            k += 1
            nums[k]=nums[i]

    return k + 1


nums = [1,1,2]
print(removeDuplicates(nums))