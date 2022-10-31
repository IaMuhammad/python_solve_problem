def sortSentence(s):
    s = s.split()
    answer = {}
    k = ''

    for item in s:
        length = len(item)
        num = item[length-1]
        
        answer[num] = item[0: length-1]
    
    string = ''
    length = len(s)
    for i in range(1, length + 1):
        i = str(i)
        string += ' ' + answer[i]
    
    return string.strip

print(sortSentence('is2 sentence4 This1 a3'))