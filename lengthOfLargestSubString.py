class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        inter = 1
        subStr = s[0:1]
        maxStr = ""
        while inter < len(s):
            char = s[inter:inter+1]
            if char in subStr:
                if len(maxStr) < len(subStr):
                    maxStr = subStr
                subStr= subStr[subStr.rindex(char)+1:]+ char
            else:
                subStr += char
            inter += 1

        return len(maxStr) if len(maxStr) > len(subStr) else len(subStr)
    
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring(" "))
    print(s.lengthOfLongestSubstring("au"))
    print(s.lengthOfLongestSubstring("dvdf"))