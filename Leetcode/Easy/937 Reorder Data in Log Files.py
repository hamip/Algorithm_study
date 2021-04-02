'''https://leetcode.com/problems/reorder-data-in-log-files/'''

'''937. Reorder Data in Log Files'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
        
        #separate letter-logs and digit-logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else: 
                letters.append(log)
        
        #sort letter-logs contents by lexicographically first;
        #if same contents, then sort by their identifiers
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letters + digits
      
