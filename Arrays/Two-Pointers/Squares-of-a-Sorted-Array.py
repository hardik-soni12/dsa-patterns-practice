'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring: [16,1,0,9,100]. After sorting: [0,1,9,16,100].
'''

def sortedSquares(nums):
    n = len(nums)
    res = [0] * n
    i,j,k = 0, n-1, n-1
    while i <= j:
        lsq, rsq = nums[i]**2, nums[j]**2
        if lsq > rsq:
            res[k] = lsq
            i +=1
        else:
            res[k] = rsq
            j -=1
        k -= 1

    return res
            

nums = [-7,-3,2,3,11]
print(sortedSquares(nums))
