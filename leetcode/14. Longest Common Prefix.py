def longestCommonPrefix(strs):
    str = strs[0]
    word = ''
    if len(strs) == 1 or len(strs) == strs.count(str):
        return strs[0]
    for i in str:
        b = False
        for each in strs:
            if each.startswith(word + i):
                b = True
            else:
                b = False
                break
            
        if b:
            word += i
        else:
            break
    
    return word
str1 = ["aaa", "aa", "aaa"]
print(longestCommonPrefix(str1))