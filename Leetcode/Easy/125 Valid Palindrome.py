'''https://leetcode.com/problems/valid-palindrome/'''

'''Leetcode #125 Valid Palindrome'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Get rid of uppercase letter
        s = s.lower()
        
        #get rid of punctuation marks
        sentence = [word for word in s if word.isalnum()]
        
        #if sentence is sames as the reversed sentence
        if sentence == sentence[::-1]:
            return True
        else:
            return False
