def isHappy(num):
    def summX(x):
        x = str(x)
        s = 0
        for item in x:
            s += int(item) * int(item)
        
        return s

    while num > 9:
        num = summX(num)
    
    if num == 1 or num == 7:
        return True
    else:
        return False

print(isHappy(10))
