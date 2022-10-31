def countEven(num):
    def SummNum(x):
        x = str(x)
        s = 0

        for item in x:
            s += int(item)
        
        return s
        
    
    if SummNum(num) % 2 == 0:
        return num // 2
    else:
        return num // 2 - 1

print(countEven(11))