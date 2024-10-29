class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_len = 1
        left = 0
        right = 1
        while right < len(s):
            if s[right] in s[left:right]:
                left += 1
            else:
                max_len = max(max_len, right - left + 1)
                right += 1
        return max_len