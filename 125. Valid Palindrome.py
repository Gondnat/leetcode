class Solution:
    def isPalindrome(self, s: str) -> bool:
        output_string = ''.join(filter(str.isalnum, s)).lower()
        return output_string == output_string[::-1]
