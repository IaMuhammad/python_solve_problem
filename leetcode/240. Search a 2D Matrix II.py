def searchMatrix(matrix, target):
    satr = len(matrix)

    def findTarget(list):
        return target in list

    for item in matrix:
        if findTarget(item) == True:
            return True
    
    return False