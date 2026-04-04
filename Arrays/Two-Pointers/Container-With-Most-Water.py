'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, 
such that the container contains the most water. Return the maximum amount of water.

Example 1

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at index 1 and 8 form the best container: min(8,7)×7 = 49.
'''

def max_area(height):
    l, r = 0, len(height)-1
    best = 0
    while l < r:
        area = min(height[l], height[r]) * (r-l)
        best = max(best, area)
        if height[l] < height[r]:
            l += 1
        else:
            r-= 1

    return best



height = [4,3,2,1,4]
print(max_area(height=height))