'''https://leetcode.com/problems/most-common-word/'''

'''819. Most Common Word'''

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # use regex to get rid of punctuation and banned words in the paragraph
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() 
                      if word not in banned]
        count = Counter(words)

        return count.most_common(1)[0][0]
