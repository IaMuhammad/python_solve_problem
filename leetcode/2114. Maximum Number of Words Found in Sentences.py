def mostWordsFound(sentences):
    amount = 0
    for item in sentences:
        if amount < len(item.split()):
            amount = len(item.split())

    return amount

srt = "alice and bob love leetcode", "i think so too", "this is great thanks very much"
print(mostWordsFound(srt))