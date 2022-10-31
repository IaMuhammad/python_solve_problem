def getDecimalValue(head):
    num = '0b' + ''.join(str(a) for a in head)
    return eval(num)

print(getDecimalValue([1,0,1,1]))