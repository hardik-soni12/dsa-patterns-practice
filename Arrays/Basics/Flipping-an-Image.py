'''
Given an n×n binary matrix image, flip each row horizontally and invert it. To flip: reverse each row. To invert: replace 0→1, 1→0 (XOR with 1).

Example 1

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: Flip [1,1,0]→[0,1,1]→invert→[1,0,0].
'''

def flipping_image(image):
    l = len(image)
    for i in range(l):
        left, right = 0, l-1
        while left <= right:
            temp = image[i][left] ^ 1
            image[i][left] = image[i][right] ^ 1
            image[i][right] = temp
            left += 1
            right -= 1
    return image

image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipping_image(image))