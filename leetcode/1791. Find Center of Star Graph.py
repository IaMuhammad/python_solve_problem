class Solution:
    def findCenter(edges):
        x = int()
        
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            x = edges[0][0]
        elif edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:
            x = edges[0][1]
        
        return x

print(Solution.findCenter([[1,2],[5,1],[1,3],[1,4]]))