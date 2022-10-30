def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrix[:] = list(map(list, zip(*matrix)))
    matrix[:] = [i[::-1] for i in matrix]