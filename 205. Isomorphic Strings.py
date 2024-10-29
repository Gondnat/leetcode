class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = dict()
        for i in range(len(s)):
            if s[i] in map:
                if map[s[i]] != t[i]:
                    return False
            else:
                if t[i] in map.values():
                    return False
                map[s[i]] = t[i]
        
        s_list = list(s)
        for i in range(len(s_list)):
            s_list[i] = map[s_list[i]]
        
        s = ''.join(s_list)
            
        return t == s
    

if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic("egg", "add")) # True
    print(s.isIsomorphic("foo", "bar")) # False
    print(s.isIsomorphic("paper", "title")) # True
    print(s.isIsomorphic("ab", "aa")) # False
    print(s.isIsomorphic("aa", "ab")) # False
    print(s.isIsomorphic("ab", "ca")) # True