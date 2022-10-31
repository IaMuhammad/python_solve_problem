def is_anagram(str1, str2) -> bool:
    str1, str2 = sorted(list(str1)), sorted(list(str2))
    return str2 == str1

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    d = {}
    for i in strs:
        k = str(sorted(i))
        if d.get(k, 0):
            d[k].append(i)
        else:
            d[k] = [i]
    strs = []
    for i in d.values():
        strs.append(i)
    return strs
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))