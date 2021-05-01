def compareTriplets(a: list, b: list):
    alice_score = 0
    bob_score = 0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
        else:
            continue
        
    return [alice_score, bob_score]
