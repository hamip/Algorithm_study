# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    pos, neg, zer = 0, 0, 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zer += 1
    
    print("%.6f"%(pos/len(arr)))
    print("%.6f"%(neg/len(arr)))
    print("%.6f"%(zer/len(arr)))
