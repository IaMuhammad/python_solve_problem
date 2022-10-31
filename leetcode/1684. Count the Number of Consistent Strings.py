def countConsistentStrings(allowed, words):
    c = 0
    for word in words:
        l = 0
        for letter in allowed:
            l += word.count(letter)
        print(len(word), l)
        if l == len(word):
            c+=1
    return c

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(countConsistentStrings(allowed, words))