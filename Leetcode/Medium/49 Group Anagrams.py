'''https://leetcode.com/problems/group-anagrams/'''

'''49. Group Anagrams'''

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)
        
        # anagrams, when sorted, have same word
        # use the sorted word as the key
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
    
        return list(anagrams.values())
    
