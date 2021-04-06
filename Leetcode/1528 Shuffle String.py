# https://leetcode.com/problems/shuffle-string/submissions/

# 1528. Shuffle String

# Initial solution
class Solution:
    def restoreString(s: str, indices: list[int]) -> str:
        words = sorted(dict(zip(indices, s)).items())
        shuffled_string = []
        for i in range(len(words)):
            shuffled_string.append(words[i][1])
    
        return "".join(shuffled_string)
    
    # cleaner solution
    def restoreString(s: str, indices: list[int]) -> str:
        res = [''] * len(s)   # to initialize and limit the size of array
        for i in range(len(s)):
            res[indices[i]] = s[i]
        
        return "".join(res)
