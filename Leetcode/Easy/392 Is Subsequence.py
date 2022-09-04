from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            if c not in t:
                return False
            
        q = deque(list(t))
        sq = deque(list(s))
        stack = []

        while sq and q:
            if q.popleft() == sq[0]:
                stack.append(sq.popleft())

        return False if len(stack) != len(s) else True
