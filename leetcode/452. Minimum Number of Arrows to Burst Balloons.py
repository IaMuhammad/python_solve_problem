def check(point1, point2):
    if point1[0] <= point2[0] and point1[1] >= point2[0]:
        return True
    return False

def findMinArrowShots(points: list[list[int]]) -> int:
    points.sort()
    c, cache = 0, points[0]
    for i in range(1, len(points)):
        if check(cache, points[i]):
            cache = [max(cache[0], points[i][0]), min(cache[1], points[i][1])]
        else:
            c += 1
            cache = points[i]
    return c + 1

print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))

"""
ℹ️ Dasturlash tili: Python 

📌 LeetCode : Substrings of Size Three with Distinct Characters

 (https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/)📊 Daraja : 🟢 Easy 

📬 Mualliflar :   (http://t.me/KhanHarry)PythonHere (https://t.me/Dilshod_Absaitov) 

✅ Usullar soni : 1 ta

Bizni kuzatishda davom eting

Telegram (https://t.me/+7vZOAqpnyOc5Mjk6) | 🔗 String (https://leetcode.com/tag/string/)
"""