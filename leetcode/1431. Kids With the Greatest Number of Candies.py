def kidsWithCandies(candies, extraCandies):
    answer = []
    for item in candies:
        if item + extraCandies >= max(candies):
            answer.append(True)
        else:
            answer.append(False)
    
    return answer

print(kidsWithCandies([2, 3, 1, 5, 3], 3))