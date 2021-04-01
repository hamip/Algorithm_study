'''https://leetcode.com/problems/valid-palindrome/'''

'''Leetcode #125 Valid Palindrome'''

'''Runtime: 36ms Memory: 15.9 MB'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Get rid of uppercase letter
        s = s.lower()
        
        #get rid of punctuation marks
        sentence = [word for word in s if word.isalnum()]
        
        #if sentence is same as the reversed sentence, return True
        return sentence == sentence[::-1]
