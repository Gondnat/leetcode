class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        maxStr = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                subStr = s[i:j]
                if subStr == subStr[::-1]:
                    if len(subStr) > len(maxStr):
                        maxStr = subStr
        return maxStr