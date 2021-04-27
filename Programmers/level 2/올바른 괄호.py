def solution(s: str) -> bool:
    stack = []
    for l in s:
        if l == '(':
            stack.append(l)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    # if all brackets are paired, the length of stack will be zero, returning True
    # if not paired, len(stack) != 0 and therefore return False
    return len(stack) == 0
  
