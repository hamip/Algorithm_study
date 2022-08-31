class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chr_set = dict()
        
        for c1, c2 in zip(s, t):
            if c1 in chr_set:
                if chr_set[c1] != c2:
                    return False
            else:
                if c2 in chr_set.values():
                    return False
                else:
                    chr_set[c1] = c2
        else:
            return True
