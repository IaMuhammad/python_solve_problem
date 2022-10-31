def countMatches(items, ruleKey, ruleValue):
    cnt = 0
    marker = {'type': 0, 'color': 1, 'name': 2}
    if ruleKey == 'type':
        for item in items:
            if item[marker[ruleKey]] == ruleValue:
                cnt += 1
    
    return cnt