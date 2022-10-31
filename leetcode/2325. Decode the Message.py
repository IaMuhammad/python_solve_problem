key = 'the quick brown fox jumps over the lazy dog'
message = 'vkbs bs t suepuv'
alp = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
key = key.split()
new_key = ''
for i in key:
    for l in i:
        b = l in new_key
        print(b, l, new_key)
        if b:
            pass
        else:
            new_key += l

print(new_key)
for i in message:
    if i != ' ':
        ind = new_key.find(i)
        ans += alp[ind]
        print(ind, ans, i)
    else:
        ans += ' '
return ans