def numberOfMatches(n):
    s = 0
    while n != 1:
        if n % 2 == 0:
            s += n // 2
            n //= 2
        else:
            s += n // 2
            n = n // 2 + 1
    
    return s

print(numberOfMatches(7))

if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            x = edges[0]
        elif edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:
            x = edges[0][1]
        
        return x