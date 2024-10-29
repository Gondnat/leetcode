from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if  len(words) == 1:
            return [words[0].ljust(maxWidth)]
        res = []
        line = []
        for i in range(len(words)):
            if len(' '.join(line)) + len(words[i]) < maxWidth:
                line.append(words[i])
            else:
                if len(line) > 0:
                    res.append(self.justify(line, maxWidth))
                line = [words[i]]
        res.append(self.justify(line, maxWidth, True))
        return res
    def justify(self, line, maxWidth, last_line=False):
        if len(line) == 1:
            return line[0].ljust(maxWidth)
        if last_line:
            return ' '.join(line).ljust(maxWidth)
        
        space = maxWidth - sum(len(word) for word in line)
        n = len(line) - 1
        q, r = divmod(space, n)
        return (' '*(q+1)).join(line[:r+1]) + ' '*q + (' '*q).join(line[r+1:])

if __name__ == '__main__':
    words = ["Listen","to","many,","speak","to","a","few."]
    print(Solution().fullJustify(words, 6))