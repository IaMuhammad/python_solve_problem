def numberOfSteps(num):
    cnt = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        
        cnt += 1

    
    return cnt

print(numberOfSteps(14))