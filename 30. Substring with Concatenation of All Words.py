class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []
        word_len = len(words[0])
        word_num = len(words)
        total_len = word_len * word_num