def countOperations(num1, num2):
    cnt = 0
    if num1 == num2:
        return 1

    while 1:
        if num1 > num2:
            num1 = num1 - num2

        elif num1 < num2:
            num2 = num2 - num1
        
        else:
            return cnt+1
        
        cnt += 1