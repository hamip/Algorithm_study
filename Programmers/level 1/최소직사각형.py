def solution(sizes: list) -> int:
    max_w, max_h = 0, 0

    for w, h in sizes:
        # 명함 회전
        if w < h:
            w, h = h, w
        # 더 큰 값을 저장
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    return max_h * max_w
