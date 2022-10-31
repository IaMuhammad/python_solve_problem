def nextGreatestLetter(letters, target):
    l = 0
    r = len(letters) - 1
    while l <= r:
        m = (l + r + 1) // 2
        if letters[m] > target and m == 0:
            return letters[0]
        elif letters[m] > target and letters[m-1] <= target:
            return letters[m]
        elif letters[m-1] > target:
            r = m - 1
        else:
            l = m + 1
    return letters[0]

print(nextGreatestLetter(["a","c","d","e"],"a"))