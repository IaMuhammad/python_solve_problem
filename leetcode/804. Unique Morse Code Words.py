co = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
words = ["gin","zen","gig","msg"]

alp = dict()
ans = set()
for i in range(26):
    alp[chr(97 + i)] = co[i]

for word in words:
    s = ''
    for letter in word:
        s += alp[letter]
    ans.add(s)

return len(ans)