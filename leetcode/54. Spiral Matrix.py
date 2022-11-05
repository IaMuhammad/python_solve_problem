def spiralOrder(matrix: list[list[int]]) -> list[int]:
    a = []
    while matrix:
        a += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return a