'''
Given sorted arrays nums1 (with m real elements + n zeros) and nums2 (n elements), merge them in-place into nums1 in non-decreasing order.

Example 1

Input: nums1=[1,2,3,0,0,0] m=3, nums2=[2,5,6] n=3
Output: [1,2,2,3,5,6]
'''

def merge_sorted_arrays(nums1,m, nums2, n):
    i,j,k = m-1, n-1, (m+n-1)
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
        
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


nums1 = [4,5,6,0,0,0]
m=3
nums2 = [1,2,3]
n=3

print(merge_sorted_arrays(nums1=nums1, m=m, nums2=nums2, n=n))