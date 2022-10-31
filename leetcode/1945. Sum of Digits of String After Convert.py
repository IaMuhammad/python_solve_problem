def getLucky(s, k):
    numStr = ''

    for item in s:
        numStr += str(ord(item) - 96)
    
    for i in range(1, k + 1):
        numInt = 0
        for item in numStr:
            numInt += int(item)

        numStr = str(numInt)
    
    return numInt


print(getLucky('iii', 1))