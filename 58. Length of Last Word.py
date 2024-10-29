class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sub_strs = s.split()
        return len(sub_strs[-1]) if sub_strs else 0