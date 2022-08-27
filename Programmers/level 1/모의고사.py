def solution(answers: list) -> list:
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0, 0, 0]
    people = []
    
    for i, ans in enumerate(answers):
        if p1[i % 5] == ans:
            correct[0] += 1
        if p2[i % 8] == ans:
            correct[1] += 1
        if p3[i % 10] == ans:
            correct[2] += 1
    
    for i in range(3):
        if max(correct) == correct[i]:
            people.append(i + 1)
            
    return people
    
