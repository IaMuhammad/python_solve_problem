from operator import index


def search(nums, target):
    

    k = nums.index(min(nums))
    nums = sorted(nums)

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = nums[mid]

        if mid_value == target:
            x = (mid + k) % len(nums)
            return x
        
        elif mid_value > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1

nums = [3, 5, 1]
print(search(nums, 5))