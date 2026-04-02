'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn], return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: x=[2,5,1], y=[3,4,7]. Interleaved: [2,3,5,4,1,7].
'''

def shuffle_the_array(nums, n):
    res = [0]* (n*2)
    for i in range(n):
        res[2*i] = nums[i]
        res[2*i+1] = nums[i+n]
    return res

nums = [2,5,1,3,4,7]
n = 3
print(shuffle_the_array(nums, n))