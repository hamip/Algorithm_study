def solution(s: str) -> str:
    words = s.split()
    altered = []

    for wrd in words:
        new = ""
        for i in range(len(wrd)):
            if i % 2 == 0:
                new += wrd[i].upper()
            else:
                new += wrd[i].lower()
        altered.append(new)
        

    return " ".join(altered)
