def sortedSquares(nums: list):
    l, r = 0, len(nums) - 1
    while l < r:
        if abs(nums[0]) > abs(nums[r]):
            nums[0], nums[r] = nums[r], nums[0]**2
        el:
            nums[r] **= 2
        r -= 1
    nums[0] **= 2
    return nums

print(sortedSquares([-5,-3,-2,-1]))

"""
            -5 -3 -2 -1
            
"""