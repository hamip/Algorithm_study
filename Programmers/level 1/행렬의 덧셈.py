def solution(arr1: list, arr2: list) -> list:
    result = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        result.append(temp)

    return result
