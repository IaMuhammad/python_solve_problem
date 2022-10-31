def truncateSentence(s, k):
    s = s.split()
    i = 0
    ans = ''
    while i < k:
        ans += s[i] + " "
        i += 1
    
    return ans.rstrip()

print(truncateSentence("Hello how are you Contestant", 4))