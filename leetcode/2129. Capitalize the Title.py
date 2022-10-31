def capitalizeTitle(title):
    title = str(title)
    title = title.lower()
    title = title.split()
    string = ''

    for item in title:
        x = item[0]
        print(len(item), item)
        if len(item) > 2:
            x = x.upper()
        
        string += x + item[1:] + ' '

    return string.rstrip()

print(capitalizeTitle("i lOve leetcode"))