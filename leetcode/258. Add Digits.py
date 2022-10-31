def addDigits(num):
    def summX(x):
        x = str(x)
        s = 0
        for item in x:
            s += int(item)
        
        return s


    while num > 9:
        num = summX(num)
    
    return num

print(addDigits(38))
