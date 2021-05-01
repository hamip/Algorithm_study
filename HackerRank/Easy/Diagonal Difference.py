def diagonalDifference(arr: list) -> int:
    first = 0
    second = 0
    i = 0
    j = 0
    while i != len(arr):
        while j != len(arr):
            first += arr[i][j]
            second += arr[::-1][i][j]
            break
        j += 1
        i += 1
        
    return abs(first - second)
