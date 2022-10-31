def xorOperation(n, start):
    nums = []
    answer = int()
    for i in range(0, n):
        nums.append(start + 2 * i)
        answer ^= nums[i]
    return answer

print(xorOperation(5, 0))