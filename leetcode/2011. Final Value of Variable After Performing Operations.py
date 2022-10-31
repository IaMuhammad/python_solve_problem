def finalValueAfterOperations(operations):
    cnt_m = 0
    cnt_p = 0
    for item in operations:

        if item.startswith('--') or item.endswith('--'):
            cnt_m = cnt_m + 1
            print(1)

        elif item.startswith('++') or item.endswith('++'):
            cnt_p = cnt_p + 1
            print(2)


        x = cnt_p - cnt_m
    print(cnt_m, cnt_p)
    return x

str1 = ["++X","X++","X++"]
print(finalValueAfterOperations(str1))