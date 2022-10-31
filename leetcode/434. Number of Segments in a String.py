def countSegments(s):
        i = 0
        cnt = 0
        while i < len(s):
            if s[i] == ' ':
                cnt += 1
            i += 1
        
        if cnt == 1:
            if (ord(s[0]) >= 65 and ord(s[0]) <= 90):
                cnt = 0
            elif (ord(s[0]) >= 97 and ord(s[0]) <= 122):
                cnt = 0
            else:
                cnt = -2

        cnt += 1
        return cnt
a = str(input())
print(countSegments(a))